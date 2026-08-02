import unittest
from unittest.mock import patch

from src import generator


class CompileQuizDataTests(unittest.TestCase):
    @patch("src.generator.query_historic_facts", return_value=["historic fact"])
    @patch("src.generator.get_live_news_context", return_value="live news")
    def test_missing_api_key_raises_clear_error(self, *_mocks):
        original_key = generator.Gemini_API_KEY
        generator.Gemini_API_KEY = None
        try:
            quiz_text, context = generator.compile_quiz_data("Cricket", "Easy")
            self.assertIn("Question:", quiz_text)
            self.assertIn("Correct Answer:", quiz_text)
            self.assertIn("historic fact", context)
        finally:
            generator.Gemini_API_KEY = original_key

    @patch("src.generator.query_historic_facts", return_value=["historic fact"])
    @patch("src.generator.get_live_news_context", return_value="live news")
    def test_geminiai_failure_falls_back_to_local_quiz(self, *_mocks):
        class FakeCompletions:
            def create(self, *args, **kwargs):
                raise RuntimeError("boom")

        class FakeClient:
            chat = type("Chat", (), {"completions": FakeCompletions()})

        with patch("src.generator.Gemini", return_value=FakeClient()):
            quiz_text, context = generator.compile_quiz_data("Cricket", "Easy")
            self.assertIn("Question:", quiz_text)
            self.assertIn("Correct Answer:", quiz_text)
            self.assertIn("historic fact", context)


if __name__ == "__main__":
    unittest.main()
