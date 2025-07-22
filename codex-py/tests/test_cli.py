import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "cli.py"


class CLITest(unittest.TestCase):
    def test_version(self):
        result = subprocess.run([sys.executable, str(CLI), "--version"], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "0.0.1")


if __name__ == "__main__":
    unittest.main()
