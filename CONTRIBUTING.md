# Contributing

Thank you for your interest in contributing to the View AI Python SDK!

The following is a set of guidelines for contributing to our project on Github. These are mostly guidelines, not rules.

## Code of Conduct

This project and everyone participating in it is governed by the Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to project moderators.

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install development dependencies:
```bash
pip install -e ".[testing]"
```
4. Install pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

## Code Style

We use several tools to maintain code quality:

- **Ruff**: For code formatting and linting
- **Pre-commit hooks**: To automate style checks
- **Type hints**: Required for all function parameters and return values

The project's code style is automatically enforced by pre-commit hooks. You can manually run the checks:

```bash
pre-commit run --all-files
```

## Pull Requests

Please follow these guidelines when submitting pull requests (PRs):

- PRs should be manageable in size to make it easy for us to validate and integrate
- Each PR should be contained to a single fix or a single feature
- Include tests for new functionality
- Update documentation as needed
- Ensure all tests pass by running `tox`
- Follow the existing code style (enforced by pre-commit hooks)
- Include a clear description of the changes and their motivation

## Testing

We use `pytest` for testing. Run the test suite:

```bash
# Run all tests
tox

# Run specific test environments
tox -e default
tox -e docs
```

## Asking Questions

Prior to asking questions, please review:
- Closed issues
- Wiki pages
- SDK documentation

If your question isn't answered in these resources, please file an issue! This helps us improve our documentation.

## Reporting Bugs

When reporting bugs, please provide the following information:

```text
--- Bug Report ---

Operating system and version: (e.g., Ubuntu 20.04)
Python version: (e.g., Python 3.8.10)
SDK version: (e.g., view-sdk 1.0.0)
Issue encountered: (What went wrong?)
Expected behavior: (What should have happened?)
Steps to reproduce: (How can we replicate the issue?)

Sample code demonstrating the problem:

import view_sdk

view_sdk.configure(
    access_key="default",
    endpoint="http://example.com",
    tenant_guid="default"
)
# Add code that demonstrates the issue

Error message and traceback: (if applicable)

--- End ---
```

## Suggesting Enhancements

When suggesting enhancements, please use this template:

```text
--- Enhancement Request ---

Enhancement request title: (Clear, descriptive title)
Use case: (Why do you want this feature?)
Current behavior: (How does it work now?)
Requested behavior: (How should it work?)
Recommended implementation: (Optional: How would you implement this?)
Usefulness of the enhancement: (Who would benefit and how?)

Example code showing desired API:

# Optional: Show how you'd like to use the new feature

--- End ---
```

## Documentation

If you're updating documentation:

1. Make changes to the relevant files in `docs/`
2. Build documentation locally to verify changes:
```bash
tox -e docs
```
3. Preview the built documentation in `docs/_build/html/`

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [Fair Core License (FCL)](https://fcl.dev/) with graduation after two years to an Apache 2.0 license.
