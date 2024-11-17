import unittest
import pandas as pd
from feedback_generator import generate_feedback

class TestFeedbackGenerator(unittest.TestCase):
    def setUp(self):
        """
        Set up test data before running the tests.
        """
        self.test_data = pd.DataFrame({
            "Name": ["Alice Smith", "Bob Johnson"],
            "Score": [85, 72],
            "Attendance": ["95%", "88%"],
            "Engagement": ["High", "Medium"]
        })

    def test_generate_feedback(self):
        """
        Test the feedback generation logic.
        """
        try:
            # Generate feedback for the test data
            feedback = generate_feedback(self.test_data)
            # Assert that the feedback is generated as a list
            self.assertIsNotNone(feedback, "Feedback generation failed.")
        except Exception as e:
            self.fail(f"Feedback generation raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

