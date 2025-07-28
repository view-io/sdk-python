from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore
from typing import List

from ...enums.embeddings_generator_enum import EmbeddingsGeneratorEnum
from ...models.semantic_cell import SemanticCellModel
from ...models.semantic_chunk import SemanticChunkModel
from ...sdk_logging import log_warning
from .langchain import Langchain
from .ollama import Ollama
from .openai import OpenAI
from .voyageai import VoyageAI


class Embeddings:
    """Embeddings resource for generating and managing embeddings."""

    _generator = None
    _api_key = None
    _endpoint = None
    _sdk_base = None
    _semaphore = None

    BATCH_SIZE = 16
    MAX_PARALLEL_TASKS = 16
    MAX_RETRIES = 3
    MAX_FAILURES = 3
    TIMEOUT = 300  # seconds

    @classmethod
    def configure(
        cls,
        generator: EmbeddingsGeneratorEnum,
        endpoint: str,
        api_key: str,
        batch_size: int = 16,
        max_parallel_tasks: int = 16,
        max_retries: int = 3,
        max_failures: int = 3,
        timeout: int = 300,
    ):
        """Configure the embeddings generator."""
        cls._generator = generator
        cls._api_key = api_key
        cls._endpoint = endpoint
        cls.BATCH_SIZE = batch_size
        cls.MAX_PARALLEL_TASKS = max_parallel_tasks
        cls.MAX_RETRIES = max_retries
        cls.MAX_FAILURES = max_failures
        cls.TIMEOUT = timeout

        cls._semaphore = Semaphore(max_parallel_tasks)

        # Initialize appropriate SDK based on generator
        if generator == EmbeddingsGeneratorEnum.LCProxy:
            cls._sdk_base = Langchain()
        elif generator == EmbeddingsGeneratorEnum.Ollama:
            cls._sdk_base = Ollama()
        elif generator == EmbeddingsGeneratorEnum.OpenAI:
            cls._sdk_base = OpenAI()
        elif generator == EmbeddingsGeneratorEnum.VoyageAI:
            cls._sdk_base = VoyageAI()
        else:
            raise ValueError(f"Unknown embeddings generator '{generator}'")

    @classmethod
    def process_semantic_cells(
        cls, cells: List[SemanticCellModel], model: str
    ) -> List[SemanticCellModel]:
        """
        Process semantic cells and generate embeddings.

        Args:
            cells: List of semantic cells to process
            model: Model to use for generating embeddings

        Returns:
            List of processed semantic cells with embeddings

        Raises:
            ValueError: If model is None or empty
            RuntimeError: If too many failures occur during processing
        """
        if not cells:
            return []
        if not model:
            raise ValueError("model cannot be None or empty")

        chunks = cls._get_chunks(cells)
        batches = [
            chunks[i : i + cls.BATCH_SIZE]
            for i in range(0, len(chunks), cls.BATCH_SIZE)
        ]
        queue = batches.copy()
        failure_count = 0
        processing_lock = Lock()
        failure_lock = Lock()

        def process_next_batch():
            nonlocal failure_count
            while True:
                batch = None
                with processing_lock:
                    if not queue:
                        return
                    batch = queue.pop(0)

                try:
                    cls._semaphore.acquire()
                    try:
                        success = cls._process_batch(model, batch)
                        if not success:
                            should_throw = False
                            with failure_lock:
                                failure_count += 1
                                if failure_count >= cls.MAX_FAILURES:
                                    should_throw = True
                            if should_throw:
                                raise RuntimeError(
                                    f"Too many failures encountered while generating embeddings using {cls._generator}. "
                                    f"Failure count: {failure_count}"
                                )
                    finally:
                        cls._semaphore.release()
                except Exception as e:
                    raise e

        try:
            # Create and start threads for parallel processing
            with ThreadPoolExecutor(
                max_workers=min(cls.MAX_PARALLEL_TASKS, len(batches))
            ) as executor:
                futures = [
                    executor.submit(process_next_batch)
                    for _ in range(min(cls.MAX_PARALLEL_TASKS, len(batches)))
                ]
                # Wait for all futures to complete and propagate any exceptions
                for future in as_completed(futures):
                    future.result()  # This will raise any exceptions that occurred
        except Exception as e:
            raise e

        return cells

    @staticmethod
    def _get_chunks(cells: List[SemanticCellModel]) -> List[SemanticChunkModel]:
        """Extract all chunks from semantic cells recursively."""
        chunks = []
        for cell in cells:
            if cell.children:
                chunks.extend(Embeddings._get_chunks(cell.children))
            if cell.chunks:
                chunks.extend(cell.chunks)
        return chunks

    @staticmethod
    def _update_chunk_embeddings(
        chunks: List[SemanticChunkModel], embeddings_map: List[dict]
    ):
        """Update chunks with their corresponding embeddings."""
        if not chunks or not embeddings_map:
            return

        content_to_embedding = {e["content"]: e["embeddings"] for e in embeddings_map}
        for chunk in chunks:
            if chunk.content in content_to_embedding:
                chunk.embeddings = content_to_embedding[chunk.content]

    @classmethod
    def _process_batch(cls, model: str, batch: List[SemanticChunkModel]) -> bool:
        """Process a batch of chunks."""
        retry_count = 0

        contents = [chunk.content for chunk in batch if chunk.content]
        embeddings_request = cls._sdk_base.REQUEST_MODEL(
            model=model, api_key=cls._api_key, contents=contents
        )

        result = None
        while retry_count < cls.MAX_RETRIES:
            try:
                result = cls._sdk_base.generate_embeddings(
                    embeddings_request, timeout=cls.TIMEOUT
                )
                if result is None:
                    log_warning(
                        f"No response from embeddings generator {cls._generator}"
                    )
                elif result.success:
                    break
                else:
                    log_warning(
                        f"Failure reported by embeddings generator {cls._generator}"
                    )
                retry_count += 1
            except Exception as e:
                log_warning(f"Error generating embeddings: {str(e)}")
                retry_count += 1

        if result and result.success:
            # Update chunk embeddings with the results
            for chunk in batch:
                if chunk.content:
                    # Find matching embedding from results
                    for i, content in enumerate(result.contents):
                        if content == chunk.content:
                            chunk.embeddings = result.embeddings[i]
                            break
            return True

        return False

    @classmethod
    def generate_embeddings(cls, embed_request):
        """
        Generate embeddings.

        Args:
            embed_request: Embeddings request containing model and contents

        Returns:
            Embeddings response
        """
        if not embed_request:
            raise ValueError("embed_request cannot be None")

        return cls._sdk_base.generate_embeddings(embed_request, cls.TIMEOUT)

    @classmethod
    def validate_connectivity(cls) -> bool:
        """
        Validate connectivity.
        Returns:
            True if connected.
        """
        return cls._sdk_base.validate_connectivity()
