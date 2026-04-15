"""Console application entry point for we123."""

from __future__ import annotations

from typing import Final

MESSAGE: Final[str] = "we123"


def main() -> int:
    """Print the fixed message once and return an exit code."""
    print(MESSAGE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
