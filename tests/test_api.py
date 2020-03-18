#!flask/bin/python
import os

import unittest
import requests
import nose



class TestCase(unittest.TestCase):
    
    # CORRECT SAMPLE API WITH 200 :
    def test_found(self):
        """
        Verify expected status code (HTTP 200 OK)
        """
        result = requests.get("https://jsonplaceholder.typicode.com/todos/1")

        expected_status_code = 200
        self.assertEqual(result.status_code, expected_status_code,
                         "Expected status code = '{}', but got '{}'".format(expected_status_code, result.status_code))

    # CORRECT SAMPLE API WITH 403 can be used for 404 also
    def test_not_found(self):
        """
        Verify expected status code (HTTP 404 Not Found)
        """
        result = requests.get("https://scontent.fsin1-1.fna.fbcdn.net/v/t1.0-9/90178918_10158231721767210_4053297655281876992_n.jpg")

        expected_status_code = 403
        self.assertEqual(result.status_code, expected_status_code,
                         "Expected status code = '{}', but got '{}'".format(expected_status_code, result.status_code))


if __name__ == '__main__':
    unittest.main()