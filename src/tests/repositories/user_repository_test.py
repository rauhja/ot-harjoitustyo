import unittest
from repositories.user_repository import UserRepository
from services.database_service import DatabaseService
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        UserRepository().delete_data()
        self.user = User(username="Player",
                         password="Passw0rd")
        DatabaseService().create_user("Player", "Passw0rd")

    def test_create_user_creates_user(self):
        user = UserRepository().find_by_username("Player")
        self.assertEqual(user.username, self.user.username)

    def test_login_failed(self):
        user_row = UserRepository().login(username="Pelaaja", password="password")
        self.assertEqual(user_row, None)

    def test_login(self):
        user_row = UserRepository().login(username="Player", password="Passw0rd")
        self.assertEqual(user_row.username, self.user.username)
