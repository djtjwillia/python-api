import unittest
import os
import json
from app import create_app

class APITestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_api_home(self):
        result = self.client().get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('This site is a demo API.', str(result.data))

    def test_api_message(self):
        result = self.client().get('/api/v1/message/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Automate all the things!', str(result.data))

if __name__ == "__main__":
    unittest.main()