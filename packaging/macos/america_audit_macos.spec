# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

from PyInstaller.utils.hooks import collect_submodules

ROOT = Path(SPECPATH)
hidden = (
    collect_submodules("webview")
    + collect_submodules("uvicorn")
    + ["Vision", "Quartz", "Foundation"]
)

datas = []
for rel in [
    "frontend/dist",
    "backend/migrations",
    "tax_rules",
    "conversion_templates",
    "rtu_patterns",
    "classification_rules",
    "accounting_catalogs",
    "sat_forms",
]:
    src = ROOT / rel
    if src.exists():
        datas.append((str(src), rel))

datas.append((str(ROOT / "backend" / "alembic.ini"), "backend"))

a = Analysis(
    [str(ROOT / "desktop" / "desktop_launcher.py")],
    pathex=[str(ROOT), str(ROOT / "backend")],
    binaries=[],
    datas=datas,
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="AmericaAudit",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="AmericaAudit",
)

app = BUNDLE(
    coll,
    name="America Audit.app",
    icon=str(ROOT / "assets" / "america_audit.icns"),
    bundle_identifier="com.americaaudit.desktop",
    info_plist={
        "CFBundleName": "America Audit",
        "CFBundleDisplayName": "America Audit",
        "CFBundleShortVersionString": "1.0.0",
        "CFBundleVersion": "1.0.0",
        "NSHighResolutionCapable": True,
        "LSMinimumSystemVersion": "12.0",
        "NSRequiresAquaSystemAppearance": False,
    },
)
