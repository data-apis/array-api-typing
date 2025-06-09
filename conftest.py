"""Pytest configuration file."""

from typing import Final

from sybil import Sybil
from sybil.parsers.doctest import DocTestParser

readme_tester: Final = Sybil(
    parsers=[DocTestParser()],
    pattern="README.md",
)

python_file_tester: Final = Sybil(
    parsers=[DocTestParser()],
    pattern="src/**/*.py",
)

pytest_collect_file: Final = (readme_tester + python_file_tester).pytest()
