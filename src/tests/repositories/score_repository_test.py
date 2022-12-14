import unittest
from repositories.score_repository import ScoreRepository
from services.database_service import DatabaseService
from entities.score import Score


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        ScoreRepository().delete_data()
        self.score = Score(username="Player")
        DatabaseService().create_score("Player")

    def test_create_score_creates_score(self):
        score = ScoreRepository().find_by_username("Player")
        self.assertEqual(score.username, self.score.username)

    def test_update_games_played_updates_score(self):
        ScoreRepository().update_played_games("Player")
        score = ScoreRepository().get_played_games("Player")
        self.assertEqual(score, 1)

    def test_update_guessed_words_updates_score(self):
        ScoreRepository().update_guessed_words("Player")
        score = ScoreRepository().get_guessed_words("Player")
        self.assertEqual(score, 1)
