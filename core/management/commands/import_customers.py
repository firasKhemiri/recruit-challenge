import os

from django.conf import settings
from django.core.management.base import BaseCommand

from core.utils.customer_utils import create_bulk_customer


class Command(BaseCommand):
    help = 'Imports customer data from a csv file into the database.'

    def handle(self, *args, **kwargs):
        """ Add the customers in the csv file specified in the args into the DB."""

        file_name = "customers.csv"

        accept = input("Would you like to add customers ? [Yes/No]")
        if accept == 'y' or accept == 'yes':
            is_path = input('Is "customers.csv" the file that you want to import ? [Yes/No]')
            if is_path == 'n' or is_path == 'no':
                file_name = input('Enter the csv file name.')
            create_bulk_customer(os.path.join(settings.BASE_DIR, 'static', file_name))
