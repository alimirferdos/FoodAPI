# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.hits import Hits  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_search(self):
        """Test case for search

        Finds recipes by query
        """
        query_string = [('query', 'query_example'),
                        ('_from', 56),
                        ('to', 56)]
        response = self.client.open(
            '/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_by_ingredient(self):
        """Test case for search_by_ingredient

        Finds recipes by ingredients
        """
        query_string = [('ingr', 'ingr_example')]
        response = self.client.open(
            '/search/findByIngredients',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_by_shopping_list(self):
        """Test case for search_by_shopping_list

        Finds recipes by shopping list
        """
        body = Object()
        response = self.client.open(
            '/search/findByShoppingList',
            method='POST',
            data=json.dumps(body),
            content_type='image/png')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
