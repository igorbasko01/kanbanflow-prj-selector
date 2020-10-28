#!/usr/bin/env python

"""Tests for `kanbanflow_prj_selector` package."""


import unittest
from click.testing import CliRunner

from kanbanflow_prj_selector import kanbanflow_prj_selector
from kanbanflow_prj_selector import cli


class TestKanbanflow_prj_selector(unittest.TestCase):
    """Tests for `kanbanflow_prj_selector` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    @unittest.skip
    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main())
        assert result.exit_code == 0
        assert 'kanbanflow_prj_selector.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
