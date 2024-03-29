# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ingredient import Ingredient  # noqa: F401,E501
from swagger_server.models.nutrient import Nutrient  # noqa: F401,E501
from swagger_server import util


class Recipe(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, uri: str=None, label: str=None, image: str=None, source: str=None, url: str=None, _yield: int=None, calories: float=None, total_weight: float=None, ingredients: List[Ingredient]=None, total_nutrients: List[Nutrient]=None, total_daily: List[Nutrient]=None, diet_labels: str=None, health_labels: str=None):  # noqa: E501
        """Recipe - a model defined in Swagger

        :param uri: The uri of this Recipe.  # noqa: E501
        :type uri: str
        :param label: The label of this Recipe.  # noqa: E501
        :type label: str
        :param image: The image of this Recipe.  # noqa: E501
        :type image: str
        :param source: The source of this Recipe.  # noqa: E501
        :type source: str
        :param url: The url of this Recipe.  # noqa: E501
        :type url: str
        :param _yield: The _yield of this Recipe.  # noqa: E501
        :type _yield: int
        :param calories: The calories of this Recipe.  # noqa: E501
        :type calories: float
        :param total_weight: The total_weight of this Recipe.  # noqa: E501
        :type total_weight: float
        :param ingredients: The ingredients of this Recipe.  # noqa: E501
        :type ingredients: List[Ingredient]
        :param total_nutrients: The total_nutrients of this Recipe.  # noqa: E501
        :type total_nutrients: List[Nutrient]
        :param total_daily: The total_daily of this Recipe.  # noqa: E501
        :type total_daily: List[Nutrient]
        :param diet_labels: The diet_labels of this Recipe.  # noqa: E501
        :type diet_labels: str
        :param health_labels: The health_labels of this Recipe.  # noqa: E501
        :type health_labels: str
        """
        self.swagger_types = {
            'uri': str,
            'label': str,
            'image': str,
            'source': str,
            'url': str,
            '_yield': int,
            'calories': float,
            'total_weight': float,
            'ingredients': List[Ingredient],
            'total_nutrients': List[Nutrient],
            'total_daily': List[Nutrient],
            'diet_labels': str,
            'health_labels': str
        }

        self.attribute_map = {
            'uri': 'uri',
            'label': 'label',
            'image': 'image',
            'source': 'source',
            'url': 'url',
            '_yield': 'yield',
            'calories': 'calories',
            'total_weight': 'totalWeight',
            'ingredients': 'ingredients',
            'total_nutrients': 'totalNutrients',
            'total_daily': 'totalDaily',
            'diet_labels': 'dietLabels',
            'health_labels': 'healthLabels'
        }
        self._uri = uri
        self._label = label
        self._image = image
        self._source = source
        self._url = url
        self.__yield = _yield
        self._calories = calories
        self._total_weight = total_weight
        self._ingredients = ingredients
        self._total_nutrients = total_nutrients
        self._total_daily = total_daily
        self._diet_labels = diet_labels
        self._health_labels = health_labels

    @classmethod
    def from_dict(cls, dikt) -> 'Recipe':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The recipe of this Recipe.  # noqa: E501
        :rtype: Recipe
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self) -> str:
        """Gets the uri of this Recipe.

        Ontology identifier  # noqa: E501

        :return: The uri of this Recipe.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this Recipe.

        Ontology identifier  # noqa: E501

        :param uri: The uri of this Recipe.
        :type uri: str
        """

        self._uri = uri

    @property
    def label(self) -> str:
        """Gets the label of this Recipe.

        Recipe title  # noqa: E501

        :return: The label of this Recipe.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this Recipe.

        Recipe title  # noqa: E501

        :param label: The label of this Recipe.
        :type label: str
        """

        self._label = label

    @property
    def image(self) -> str:
        """Gets the image of this Recipe.

        Image URL  # noqa: E501

        :return: The image of this Recipe.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this Recipe.

        Image URL  # noqa: E501

        :param image: The image of this Recipe.
        :type image: str
        """

        self._image = image

    @property
    def source(self) -> str:
        """Gets the source of this Recipe.

        Source site identifier  # noqa: E501

        :return: The source of this Recipe.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this Recipe.

        Source site identifier  # noqa: E501

        :param source: The source of this Recipe.
        :type source: str
        """

        self._source = source

    @property
    def url(self) -> str:
        """Gets the url of this Recipe.

        Original recipe URL  # noqa: E501

        :return: The url of this Recipe.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Recipe.

        Original recipe URL  # noqa: E501

        :param url: The url of this Recipe.
        :type url: str
        """

        self._url = url

    @property
    def _yield(self) -> int:
        """Gets the _yield of this Recipe.

        Number of servings  # noqa: E501

        :return: The _yield of this Recipe.
        :rtype: int
        """
        return self.__yield

    @_yield.setter
    def _yield(self, _yield: int):
        """Sets the _yield of this Recipe.

        Number of servings  # noqa: E501

        :param _yield: The _yield of this Recipe.
        :type _yield: int
        """

        self.__yield = _yield

    @property
    def calories(self) -> float:
        """Gets the calories of this Recipe.

        Total energy, kcal  # noqa: E501

        :return: The calories of this Recipe.
        :rtype: float
        """
        return self._calories

    @calories.setter
    def calories(self, calories: float):
        """Sets the calories of this Recipe.

        Total energy, kcal  # noqa: E501

        :param calories: The calories of this Recipe.
        :type calories: float
        """

        self._calories = calories

    @property
    def total_weight(self) -> float:
        """Gets the total_weight of this Recipe.

        Total weight, g  # noqa: E501

        :return: The total_weight of this Recipe.
        :rtype: float
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight: float):
        """Sets the total_weight of this Recipe.

        Total weight, g  # noqa: E501

        :param total_weight: The total_weight of this Recipe.
        :type total_weight: float
        """

        self._total_weight = total_weight

    @property
    def ingredients(self) -> List[Ingredient]:
        """Gets the ingredients of this Recipe.

        Ingredients list  # noqa: E501

        :return: The ingredients of this Recipe.
        :rtype: List[Ingredient]
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: List[Ingredient]):
        """Sets the ingredients of this Recipe.

        Ingredients list  # noqa: E501

        :param ingredients: The ingredients of this Recipe.
        :type ingredients: List[Ingredient]
        """

        self._ingredients = ingredients

    @property
    def total_nutrients(self) -> List[Nutrient]:
        """Gets the total_nutrients of this Recipe.

        Total nutrients for the entire recipe  # noqa: E501

        :return: The total_nutrients of this Recipe.
        :rtype: List[Nutrient]
        """
        return self._total_nutrients

    @total_nutrients.setter
    def total_nutrients(self, total_nutrients: List[Nutrient]):
        """Sets the total_nutrients of this Recipe.

        Total nutrients for the entire recipe  # noqa: E501

        :param total_nutrients: The total_nutrients of this Recipe.
        :type total_nutrients: List[Nutrient]
        """

        self._total_nutrients = total_nutrients

    @property
    def total_daily(self) -> List[Nutrient]:
        """Gets the total_daily of this Recipe.

        % daily value for the entire recipe  # noqa: E501

        :return: The total_daily of this Recipe.
        :rtype: List[Nutrient]
        """
        return self._total_daily

    @total_daily.setter
    def total_daily(self, total_daily: List[Nutrient]):
        """Sets the total_daily of this Recipe.

        % daily value for the entire recipe  # noqa: E501

        :param total_daily: The total_daily of this Recipe.
        :type total_daily: List[Nutrient]
        """

        self._total_daily = total_daily

    @property
    def diet_labels(self) -> str:
        """Gets the diet_labels of this Recipe.

        Diet labels (labels are per serving)  # noqa: E501

        :return: The diet_labels of this Recipe.
        :rtype: str
        """
        return self._diet_labels

    @diet_labels.setter
    def diet_labels(self, diet_labels: str):
        """Sets the diet_labels of this Recipe.

        Diet labels (labels are per serving)  # noqa: E501

        :param diet_labels: The diet_labels of this Recipe.
        :type diet_labels: str
        """
        allowed_values = ["balanced", "high-protein", "high-fiber", "low-fat", "low-carb", "low-sodium"]  # noqa: E501
        if diet_labels not in allowed_values:
            raise ValueError(
                "Invalid value for `diet_labels` ({0}), must be one of {1}"
                .format(diet_labels, allowed_values)
            )

        self._diet_labels = diet_labels

    @property
    def health_labels(self) -> str:
        """Gets the health_labels of this Recipe.

        Health labels (labels are per serving)  # noqa: E501

        :return: The health_labels of this Recipe.
        :rtype: str
        """
        return self._health_labels

    @health_labels.setter
    def health_labels(self, health_labels: str):
        """Sets the health_labels of this Recipe.

        Health labels (labels are per serving)  # noqa: E501

        :param health_labels: The health_labels of this Recipe.
        :type health_labels: str
        """
        allowed_values = ["vegan", "vegetarian", "paleo", "dairy-free", "gluten-free", "wheat-free", "fat-free", "low-sugar", "egg-free", "peanut-free", "tree-nut-free", "soy-free", "fish-free", "shellfish-free"]  # noqa: E501
        if health_labels not in allowed_values:
            raise ValueError(
                "Invalid value for `health_labels` ({0}), must be one of {1}"
                .format(health_labels, allowed_values)
            )

        self._health_labels = health_labels
