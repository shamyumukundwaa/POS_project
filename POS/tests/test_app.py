import os
import unittest
import uuid

os.environ.setdefault("DATABASE_URL", "sqlite:///./test_pos.db")

from fastapi.testclient import TestClient

from main import app


class AppTests(unittest.TestCase):
    def test_root_endpoint(self):
        client = TestClient(app)
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "online")

    def test_users_endpoint_returns_ok_response(self):
        client = TestClient(app)
        response = client.get("/users/")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_partial_user_update_works(self):
        client = TestClient(app)
        email = f"partial-{uuid.uuid4().hex}@example.com"

        create_response = client.post(
            "/users/",
            json={
                "full_name": "Original Name",
                "email": email,
                "password_hash": "hashed-password",
                "role": "staff",
            },
        )
        self.assertEqual(create_response.status_code, 201)

        user_id = create_response.json()["user_id"]
        update_response = client.patch(
            f"/users/{user_id}",
            json={"full_name": "Updated Name"},
        )

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["full_name"], "Updated Name")
        self.assertEqual(update_response.json()["email"], email)


if __name__ == "__main__":
    unittest.main()
