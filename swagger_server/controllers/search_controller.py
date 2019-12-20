import connexion
import six

from swagger_server.models.hits import Hits  # noqa: E501
from swagger_server import util


def search(query, _from=None, to=None):  # noqa: E501
    """Finds recipes by query

     # noqa: E501

    :param query: Query values that need to be considered for filter
    :type query: str
    :param _from: First result index. The maximum value of the “from” parameter is limitted by the number of results a plan is entitled to.
    :type _from: int
    :param to: Last result index (exclusive)
    :type to: int

    :rtype: Hits
    """
    return 'do some magic!'


def search_by_ingredient(ingr):  # noqa: E501
    """Finds recipes by ingredients

     # noqa: E501

    :param ingr: 
    :type ingr: List[str]

    :rtype: Hits
    """
    return 'do some magic!'


def search_by_shopping_list(body):  # noqa: E501
    """Finds recipes by shopping list

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Hits
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
