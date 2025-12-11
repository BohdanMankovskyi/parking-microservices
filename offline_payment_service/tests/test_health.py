import sys
import os
import types


class DummyCursor:
    def execute(self, *args, **kwargs):
        return None

    def fetchone(self):
        return None

    def fetchall(self):
        return []

    def close(self):
        return None


class DummyConn:
    def cursor(self):
        return DummyCursor()

    def commit(self):
        return None

    def close(self):
        return None


# Ensure project root on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Stub pyodbc before importing app to avoid real DB
sys.modules["pyodbc"] = types.SimpleNamespace(connect=lambda *a, **k: DummyConn())

import app


def test_health():
    app.app.config["TESTING"] = True
    client = app.app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json().get("status") == "ok"
