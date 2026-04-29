"""Unit tests for the emotion_detector function."""

import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def _mock_response(self, dominant):
        """Create a mock API response with the given dominant emotion."""
        scores = {"anger": 0.1, "disgust": 0.1, "fear": 0.1, "joy": 0.1, "sadness": 0.1}
        scores[dominant] = 0.9
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = (
            '{"emotionPredictions": [{"emotion": {"anger": '
            + str(scores["anger"])
            + ', "disgust": '
            + str(scores["disgust"])
            + ', "fear": '
            + str(scores["fear"])
            + ', "joy": '
            + str(scores["joy"])
            + ', "sadness": '
            + str(scores["sadness"])
            + "}}]}"
        )
        return mock_resp

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_emotion(self, mock_post):
        """Test that joy is correctly detected as the dominant emotion."""
        mock_post.return_value = self._mock_response("joy")
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger_emotion(self, mock_post):
        """Test that anger is correctly detected as the dominant emotion."""
        mock_post.return_value = self._mock_response("anger")
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust_emotion(self, mock_post):
        """Test that disgust is correctly detected as the dominant emotion."""
        mock_post.return_value = self._mock_response("disgust")
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness_emotion(self, mock_post):
        """Test that sadness is correctly detected as the dominant emotion."""
        mock_post.return_value = self._mock_response("sadness")
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear_emotion(self, mock_post):
        """Test that fear is correctly detected as the dominant emotion."""
        mock_post.return_value = self._mock_response("fear")
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
