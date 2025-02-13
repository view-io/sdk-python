from enum import Enum


class DocumentTypeEnum(str, Enum):
    """Data type associated with an input object or file."""

    Unknown = "Unknown"  # Unknown
    Csv = "Csv"  # CSV
    DataTable = "DataTable"  # DataTable
    Docx = "Docx"  # DOCX, Word document
    Html = "Html"  # HTML
    Json = "Json"  # JSON
    Parquet = "Parquet"  # Parquet
    Pdf = "Pdf"  # PDF
    Pptx = "Pptx"  # PPTX, PowerPoint presentation
    Sqlite = "Sqlite"  # Sqlite database file
    Text = "Text"  # Text
    Xlsx = "Xlsx"  # XLSX, Excel spreadsheet
    Xml = "Xml"  # XML
