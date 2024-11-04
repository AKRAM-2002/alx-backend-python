#!/usr/bin/env python3
"""
4. Parameterize and patch as decorators module
"""
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import json 


class TestGithubOrgClient(unittest.TestCase):
    '''
    Test the GithubOrgClient class
    '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """ Test that the result of public_repos is the expected one
        based on the mocked payload
        """
        payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_public.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license",  True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected_result):
        """ Test for the GithubOrgClient.has_license function to check
        that it returns the expected result."""
        test_class = GithubOrgClient('test')
        result = test_class.has_license(repo, license)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test class for integration tests of GithubOrgClient """
    
    @classmethod
    def setUpClass(cls):
        """ Setup method for integration tests """
        config = {'return_value.json.side_effect':
                    [
                        cls.org_payload, cls.repos_payload,
                        cls.org_payload, cls.repos_payload
                    ]
                }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop() 