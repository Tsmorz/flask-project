"""Test the main program."""

from flask_project.app import main


def test_main():
    """Test the main function."""
    assert main() is None
