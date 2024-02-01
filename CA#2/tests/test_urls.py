from flask import request


def test_home(client):
    """Test to see if server is up."""
    assert client.get("/").status_code == 200


def test_personal(client):
    """Test personal page for 200 code (all ok)."""
    assert client.get("/personal").status_code == 200


def test_cv(client):
    """Test cv page for 200 code (all ok)."""
    assert client.get("/cv").status_code == 200


def test_technologies(client):
    """Test technologies page for 200 code (all ok)."""
    assert client.get("/technologies").status_code == 200


def test_java(client):
    """Test java page for 200 code (all ok)."""
    assert client.get("/java").status_code == 200


def test_html(client):
    """Test html page for 200 code (all ok)."""
    assert client.get("/html").status_code == 200


def test_os(client):
    """Test os page for 200 code (all ok)."""
    assert client.get("/os").status_code == 200


def test_interests(client):
    """Test interests page for 200 code (all ok)."""
    assert client.get("/interests").status_code == 200


def test_showform(client):
    """Test form page for 200 code (all ok)."""
    assert client.get("/showform").status_code == 200


def test_processform(client):
    """Test form porcessing page for 200 code (all ok)."""
    assert client.get("/processform").status_code == 200


def test_messageboard(client):
    """Test meassageboard page for 200 code (all ok)."""
    assert client.get("/messageboard").status_code == 200


def test_correct_form(client):
    """Test the form page to see if it recived the correct form."""
    response = client.get("/showform")
    assert response.status_code == 200


def test_form_operation_first(client):
    """Create sample data, to send to server adn test response. """
    form_data = {
        "first": "testing",
        "last": "Doogue",
        "email": "r.doogue@gmail.com",
        "message": "Testing with pytest",
    }
    response = client.post("/processform", data=form_data)
    assert request.method == "GET"
    resp = response.data
    assert resp.startswith(b"<!DOCTYPE html>")
    assert form_data["first"] in resp
    assert form_data["last"] in resp
    assert form_data["email"] in resp
    assert form_data["message"] in resp
