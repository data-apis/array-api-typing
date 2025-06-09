"""Pytest configuration file."""

from sybil import Sybil
from sybil.parsers.doctest import DocTestParser

readme_tester = Sybil(
    parsers=[DocTestParser()],
    pattern="README.md",
)

python_file_tester = Sybil(
    parsers=[DocTestParser()],
    pattern="src/**/*.py",
)

pytest_collect_file = (readme_tester + python_file_tester).pytest()
