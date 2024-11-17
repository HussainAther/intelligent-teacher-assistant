import unittest
import pandas as pd
from summarizer import summarize_performance

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        """
        Set up test data before running the tests.
        """
        self.test_data = pd.DataFrame({
            "Name": ["Alice Smith", "Bob Johnson", "Charlie Lee"],
            "Score": [85, 72, 64],
            "Attendance": ["95%", "88%", "80%"],
            "Engagement": ["High", "Medium", "Low"]
        })

    def test_summarize_performance(self):
        """
        Test the summarization logic.
        """
        try:
            # Generate summary for the test data
            summary = summarize_performance(self.test_data)
            # Check if summary contains expected keys
            self.assertIn("Score", summary, "Summary does not contain 'Score'.")
            self.assertIn("Attendance", summary, "Summary does not contain 'Attendance'.")
        except Exception as e:
            self.fail(f"Summarization raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

