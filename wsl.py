"""
Verify that all example run scripts work correctly
"""

import sys
from sys import platform
from os import environ
from pathlib import Path
from subprocess import check_call, STDOUT
import unittest
from shutil import which


class TestExamples(unittest.TestCase):
    """
    Verify that example run scripts work correctly
    """

    def setUp(self):
        self.shell = ['bash'] if platform == 'win32' else []

        print('\n::group::Log')
        sys.stdout.flush()

    def tearDown(self):
        print('\n::endgroup::')
        sys.stdout.flush()

    def _sh(self, args):
        check_call(self.shell + args, stderr=STDOUT)

    def test_wsl_conflict(self):
        self._sh([str(Path(__file__).parent / 'wsl.sh')])
