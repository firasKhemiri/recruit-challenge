from unittest import TestCase

from core.utils.customer_utils import get_coordinates_from_city


class CoordinationTests(TestCase):

    def test_get_coords_from_city(self):
        coords = get_coordinates_from_city('Warner, NH')
        self.assertNotEqual(coords, {'lat': 0.0, 'lng': 0.0})

    def test_get_coords_from_non_existent_city(self):
        coords = get_coordinates_from_city("3abla")
        self.assertEqual(coords, {'lat': 0.0, 'lng': 0.0})

