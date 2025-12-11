import os
import sys
import types

# Add service root to import path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


class DummyCursor:
    def execute(self, *args, **kwargs):
        return None

    def close(self):
        return None


class DummyConn:
    def cursor(self):
        return DummyCursor()

    def commit(self):
        return None

    def close(self):
        return None


# Stub pyodbc.connect so init_db uses a fake connection
sys.modules["pyodbc"] = types.SimpleNamespace(connect=lambda *a, **k: DummyConn())

from app import app


def test_health():
    app.config["TESTING"] = True
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json().get("status") == "ok"
