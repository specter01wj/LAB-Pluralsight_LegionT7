import unittest
from unittest.mock import patch
from process_transcript import chat_completions_request
import openai

class TestChatCompletionRequest(unittest.TestCase):
    def test_retry_functionality(self):
        """
        Test the retry functionality of the `chat_completions_request` function.

        This test verifies that `chat_completions_request` properly retries after 
        encountering an APIConnectionError, and that it correctly limits the number of retries.
        
        The `client.chat.completions.create` method and `time.sleep` function are mocked 
        to raise a specific error and avoid delays during testing, respectively.

        Raises
        ------
        openai.APIConnectionError
            If `chat_completions_request` doesn't handle the APIConnectionError correctly.

        Notes
        -----
        This test also checks that `time.sleep` is called the correct number of times,
        which should be one less than the number of times `client.chat.completions.create` is called.
        """
        with (
            patch('process_transcript.client.chat.completions.create') as mock_create,
            patch("process_transcript.time.sleep") as mock_sleep
        ):
            # Set up the mocked method to raise an APIError
            mock_create.side_effect = openai.APIConnectionError(request=None)
            
            messages = [{"role": "user", "content": "Hi!"}]

            # Assert that the function under test raises a RetryError
            with self.assertRaises(openai.APIConnectionError):
                chat_completions_request(messages)
                
            # Check that the mocked method was called the correct number of times
            self.assertEqual(mock_create.call_count, 3)
            # Check that `time.sleep` was called one less time than the mocked method
            self.assertEqual(mock_sleep.call_count, 2)

if __name__ == "__main__":
    unittest.main()
