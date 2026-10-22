"""Basic CLI for research scans."""

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="AIxTech crypto intel v0.40 (paper-only)")
    parser.add_argument("command", choices=["scan", "brief", "posture", "version"])
    parser.add_argument("fixture", nargs="?", help="Path to synthetic fixture")
    args = parser.parse_args()

    if args.command == "version":
        from crypto_intel import __version__
        print(__version__)
        return

    print(f"Paper-only research command: {args.command}")
    if args.fixture:
        path = Path(args.fixture)
        if path.exists():
            data = json.loads(path.read_text())
            print(f"Loaded fixture with {len(data) if isinstance(data, list) else 'object'} records (SYNTHETIC expected)")
        else:
            print("Fixture not found; using in-memory synthetic example.")
    print("No live orders possible. See docs for asset-class rules and security architecture.")


if __name__ == "__main__":
    main()
