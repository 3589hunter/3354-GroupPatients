import pytest

from .forms import Bookingform
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from unittest.mock import patch

                                                                        #Create your tests here.
class testClass:
    def test_my_function(mocker):
    # Create a mock object for the class containing is_valid()
        mocker.patch('path.to.module.is_valid', return_value=True)

    # Mock the requests.post function
        mock_post = mocker.patch('requests.post')
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'success': True}

    # Use the mock object in your test
        result = Bookingform(mock_post)

    # Assert the expected behavior based on the mocked is_valid()
        assert result == "Valid"

# Create your tests here.

