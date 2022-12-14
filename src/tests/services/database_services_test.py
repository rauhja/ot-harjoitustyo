import unittest
from repositories.user_repository import UserRepository
from services.database_service import DatabaseService, InvalidPassword, InvalidLogin, UsernameExistError, UsernameTooShortError
from entities.user import User


class TestDatabaseServices(unittest.TestCase):
    def setUp(self):
        self.db_services = DatabaseService()
        UserRepository().delete_data()
        self.user = User(username="Player",
                         password="Passw0rd")
        self.db_services.create_user("Player", "Passw0rd")

    def test_login_with_valid_password(self):
        user = self.db_services.login(self.user.username, self.user.password)
        self.assertEqual(user.username, self.user.username)

    def test_login_with_invalid_password(self):
        with self.assertRaises(InvalidLogin):
            self.db_services.login(self.user.username, "password")

    def test_get_current_user(self):
        self.db_services.login(self.user.username, self.user.password)
        user = self.db_services.get_current_user
        self.assertEqual(user.username, self.user.username)

    def test_logout(self):
        self.db_services.logout()
        self.assertEqual(None, self.db_services.get_current_user)

    def test_create_user_with_too_short_password(self):
        with self.assertRaises(InvalidPassword):
            self.db_services.create_user("Tester", "Pass")

    def test_create_user_with_invalid_password_no_uppercase(self):
        with self.assertRaises(InvalidPassword):
            self.db_services.create_user("Tester", "passw0rd")

    def test_create_user_with_invalid_password_no_lowercase(self):
        with self.assertRaises(InvalidPassword):
            self.db_services.create_user("Tester", "PASSW0RD")

    def test_create_user_with_invalid_password_no_number(self):
        with self.assertRaises(InvalidPassword):
            self.db_services.create_user("Tester", "Password")

    def test_create_user_with_too_short_username(self):
        with self.assertRaises(UsernameTooShortError):
            self.db_services.create_user("t", "Passw0rd")

    def test_create_user_with_too_short_username(self):
        with self.assertRaises(UsernameExistError):
            self.db_services.create_user("Player", "Passw0rd")
