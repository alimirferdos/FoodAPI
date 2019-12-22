import connexion
import six
import requests
import tempfile

from swagger_server.models.hits import Hits  # noqa: E501
from swagger_server import util
from swagger_server.external_apis.py_edamam import Edamam
from dotenv import load_dotenv
load_dotenv()
import os
OCR_KEY = os.getenv("OCR_KEY")


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
    e = Edamam()
    return e.search_recipe(query)


def search_by_ingredient(ingr):  # noqa: E501
    """Finds recipes by ingredients

     # noqa: E501

    :param ingr: 
    :type ingr: List[str]

    :rtype: Hits
    """
    url = 'http://www.recipepuppy.com/api/?i=' + ",".join(ingr)

    r = requests.get(url).json()
    if len(r["results"]) == 0:
        pass
    result = Hits(q=ingr, count=len(r["results"]), hits=[])
    for i in r["results"]:
        result.hits.append(search(i["title"]))
    return result


def search_by_shopping_list(body):  # noqa: E501
    """Finds recipes by shopping list

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Hits
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    
    payload = {'isOverlayRequired': False,
               'apikey': OCR_KEY,
               'language': "eng",
               'iscreatesearchablepdf': False,
               'issearchablepdfhidetextlayer': False,
               'filetype': 'png'
               }

    with open("list.png", "wb") as f:
        f.write(body)

    with open("list.png", 'rb') as f:
        r = requests.post(
            'https://api.ocr.space/parse/image',
            files={'filename': f},
            data=payload,
        )

    # print(response.text)
    return search_by_ingredient(r.json()['ParsedResults'][0]['ParsedText'].split("\r\n"))
