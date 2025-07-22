import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

try:
    from .version import CLI_VERSION
except ImportError:  # Allow running as a script
    sys.path.append(str(Path(__file__).resolve().parent))
    from version import CLI_VERSION


def run_singlepass():
    print("Running Codex in single pass mode (not fully implemented)")


def run_interactive():
    print("Running Codex in interactive mode (not fully implemented)")


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if sys.version_info < (3, 10):
        sys.stderr.write(
            f"Codex CLI requires Python 3.10 or newer. You are running {sys.version}.\n"
        )
        return 1

    load_dotenv()

    parser = argparse.ArgumentParser(
        prog="codex-py",
        description="Python reimplementation of Codex CLI (simplified)",
    )
    parser.add_argument("--version", action="store_true", help="Show CLI version")
    parser.add_argument(
        "--singlepass", action="store_true", help="Run Codex in single pass mode"
    )

    args = parser.parse_args(argv)

    if args.version:
        print(CLI_VERSION)
        return 0

    if args.singlepass:
        run_singlepass()
    else:
        run_interactive()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
