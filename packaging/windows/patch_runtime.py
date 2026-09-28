from pathlib import Path

path = Path("src/AmericaAudit_Desktop_1.0.0/desktop/desktop_launcher.py")
text = path.read_text(encoding="utf-8")

changes = 0

old_uvicorn = 'config=uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning", access_log=False)'
new_uvicorn = 'config=uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning", access_log=False, log_config=None)'

if old_uvicorn in text:
    text = text.replace(old_uvicorn, new_uvicorn, 1)
    changes += 1
elif new_uvicorn not in text:
    raise SystemExit("Expected uvicorn.Config line not found; refusing silent patch.")

old_health = '/api/v1/system/health'
new_health = '/api/v1/health'

if old_health in text:
    text = text.replace(old_health, new_health, 1)
    changes += 1
elif new_health not in text:
    raise SystemExit("Expected health-check URL not found; refusing silent patch.")

path.write_text(text, encoding="utf-8")

print(f"Patched desktop launcher ({changes} change(s)):")
print("- disabled Uvicorn dictConfig inside frozen app")
print("- corrected readiness URL to /api/v1/health")
