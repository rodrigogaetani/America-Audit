from __future__ import annotations

import os
import sys
from pathlib import Path

APP_DIRNAME = "AmericaAudit"


def resource_root() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[1]


def data_root() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / APP_DIRNAME
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
        return base / APP_DIRNAME
    base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return base / APP_DIRNAME


def ensure_dirs() -> dict[str, Path]:
    root = data_root()
    paths = {
        name: root / name
        for name in ("database", "documents", "imports", "exports", "backups", "logs", "config")
    }
    root.mkdir(parents=True, exist_ok=True)
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return {"root": root, **paths}
