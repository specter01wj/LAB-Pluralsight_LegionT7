import math
import time
import openai
from tenacity import RetryError
from process_transcript import chat_completions_request
import unittest
from unittest.mock import patch, MagicMock

class TestChatCompletionRequest(unittest.TestCase):
    """
    A class used to test the function chat_completions_request from the 
    module process_transcript_retry.

    ...

    Attributes
    ----------
    retry_count : int
        a static value to determine how many times to retry the request
    multiplier : int
        a static value used as a base for exponential backoff
    exp_base : int
        a static value used as exponent for exponential backoff
    min_wait_time : int
        minimum wait time between retry attempts
    max_wait_time : int
        maximum wait time between retry attempts

    Methods
    -------
    test_successful_request(mock_create)
        Test case for successful chat completion request.
        
    test_api_error_request(mock_create)
        Test case for chat completion request that raises an APIError.
        
    test_exponential_wait(mock_create)
        Test case for the waiting mechanism of retries (exponential backoff).
        
    calculate_total_retry_time()
        Calculate the total waiting time for retry attempts.
    """
    retry_count = 3
    multiplier = 2
    exp_base = 2
    min_wait_time = 2
    max_wait_time = 30

    @patch('process_transcript.client.chat.completions.create')
    def test_successful_request(self, mock_create):
        """Test case for successful chat completion request.

        Parameters
        ----------
        mock_create : MagicMock
            a mock for the 'client.chat.completions.create' method
        """
        print("Executing test_successful_request")
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

        # Mock the return value of 'client.chat.completions.create'
        mock_create.return_value = MagicMock(choices=[MagicMock(message="Test message")])

        # Invoke the function under test
        response_message = chat_completions_request(messages)

        # Assert that the function under test returns the correct value
        self.assertEqual(response_message, "Test message")

        # Assert that 'client.chat.completions.create' was called exactly once
        mock_create.assert_called_once()
    
    @patch('process_transcript.client.chat.completions.create')
    def test_api_error_request(self, mock_create):
        """Test case for chat completion request that raises an APIConnectionError.

        Parameters
        ----------
        mock_create : MagicMock
            a mock for the 'client.chat.completions.create' method
        """
        print("Executing test_api_error_request")
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

        # Make the create method raise an APIConnectionError with the dummy request
        mock_create.side_effect = openai.APIConnectionError(request=None)

        # Assert that the function under test raises a RetryError
        with self.assertRaises(RetryError):
            chat_completions_request(messages)

        # Assert that 'client.chat.completions.create' was called exactly 'retry_count' times
        self.assertEqual(mock_create.call_count, self.retry_count)

    @patch('process_transcript.client.chat.completions.create')
    def test_exponential_wait(self, mock_create):
        """Test case for the waiting mechanism of retries (exponential backoff).

        Parameters
        ----------
        mock_create : MagicMock
            a mock for the 'client.chat.completions.create' method
        """
        print("Executing test_exponential_wait")
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

        # Mock the 'client.chat.completions.create' to throw an APITimeoutError error
        mock_create.side_effect = openai.APITimeoutError(request=None)

        start_time = time.time()
        # Assert that the function under test raises a RetryError
        with self.assertRaises(RetryError):
            chat_completions_request(messages)
        end_time = time.time()

        # Compute the total time spent in the test
        total_time = end_time - start_time

        # Compute the total time that should have been spent in retries
        total_retry_time = self.calculate_total_retry_time()

        # Assert that the total time is between min_wait_time and total_retry_time
        self.assertGreaterEqual(math.floor(total_time), self.min_wait_time)
        self.assertLessEqual(math.floor(total_time), total_retry_time)

    def calculate_total_retry_time(self):
        """Calculate the total waiting time for retry attempts.

        Returns
        -------
        int
            Total waiting time
        """
        total_wait = 0
        for attempt in range(self.retry_count-1):
            # Calculate wait time for each attempt
            wait_time = self.multiplier * math.pow(self.exp_base, attempt)
            # Ensure wait_time is within the bounds of min_wait_time and max_wait_time
            wait_time = max(self.min_wait_time, min(self.max_wait_time, wait_time))
            
            # Accumulate the total wait time
            total_wait += wait_time
        return total_wait

if __name__ == "__main__":
    unittest.main()
