import io
import os
import sys

# Ensure project root on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def test_health():
    import ocr_server as app_mod

    app_mod.app.config["TESTING"] = True
    client = app_mod.app.test_client()

    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json().get("status") == "ok"


def test_recognize_stub(monkeypatch):
    import ocr_server as app_mod

    app_mod.app.config["TESTING"] = True
    client = app_mod.app.test_client()

    # Stub subprocess call to avoid invoking real OCR
    def fake_check_output(args, text=True):
        return "DUMMY123\n"

    monkeypatch.setattr("ocr_server.subprocess.check_output", fake_check_output)

    data = {
        "image": (io.BytesIO(b"fakeimage"), "test.jpg"),
    }

    resp = client.post("/recognize", data=data, content_type="multipart/form-data")
    assert resp.status_code == 200
    assert resp.get_json().get("plate") == "DUMMY123"
