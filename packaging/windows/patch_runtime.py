from pathlib import Path

path = Path("src/AmericaAudit_Desktop_1.0.0/desktop/desktop_launcher.py")
text = path.read_text(encoding="utf-8")

old = 'config=uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning", access_log=False)'
new = 'config=uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning", access_log=False, log_config=None)'

if old not in text:
    raise SystemExit("Expected uvicorn.Config line not found; refusing silent patch.")

path.write_text(text.replace(old, new, 1), encoding="utf-8")
print("Patched desktop launcher: disabled Uvicorn dictConfig inside frozen Windows app.")
