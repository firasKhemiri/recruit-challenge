import os
from unittest import TestCase

from django.conf import settings

from core.models import Customer
from core.utils.customer_utils import create_bulk_customer


class ImportCustomersTests(TestCase):

    def test_import_customers_from_csv(self):
        create_bulk_customer(os.path.join(settings.BASE_DIR, 'static', 'customers-test.csv'))
        self.assertEqual(Customer.objects.all().count(), 10)

        self.assertNotEqual(Customer.objects.get(id=1).lat, 0.0)
