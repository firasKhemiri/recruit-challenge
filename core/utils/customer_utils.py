import csv

from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from geopy.geocoders import Nominatim

from core.models import Customer


def create_bulk_customer(file_path: str):
    """ Get all the customers in teh csv file and add them to the database."""
    try:
        with open(file_path, "r") as customers_list:
            reader = csv.reader(customers_list)
            next(reader, None)  # Skip the header of the csv file.

            for row in reader:
                coordinates = get_coordinates_from_city(row[6])
                customer, created = Customer.objects.update_or_create(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    gender=row[4],
                    company=row[5],
                    city=row[6],
                    title=row[7],

                    defaults={
                        'lat': coordinates.get('lat'),
                        'lng': coordinates.get('lng')
                    }
                )
                if not created:
                    customer.save()
    except FileNotFoundError:
        print('File not found.')


def get_coordinates_from_city(city: str):
    """ Use GeoPy to get Coordinates"""
    geo_locator = Nominatim()

    try:
        location = geo_locator.geocode(city)
        lat = location.latitude
        lng = location.longitude
    except AttributeError:
        print("Location Not Found")
        lat = 0.0
        lng = 0.0

    except GeocoderTimedOut:
        print("Timeout Error")
        lat = 0.0
        lng = 0.0

    except GeocoderServiceError:
        print("Timeout Error")
        lat = 0.0
        lng = 0.0

    return {
        "lat": lat,
        'lng': lng
    }
