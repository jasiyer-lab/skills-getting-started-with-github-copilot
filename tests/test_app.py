from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email():
    # Arrange
    activity_name = "Chess Club"
    email = "teststudent@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    delete_response = client.delete(f"/activities/{activity_name}/participants?email={email}")
    activities = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert delete_response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_unregister_participant_returns_error_when_missing():
    # Arrange
    activity_name = "Programming Class"
    email = "missingstudent@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 404
