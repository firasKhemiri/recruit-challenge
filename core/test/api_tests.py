import json

from graphene_django.utils.testing import GraphQLTestCase

from core.models import Customer
from recruit_challenge.schema import schema


class APITests(GraphQLTestCase):

    def setUp(self):
        Customer.objects.create(id=1, first_name="John", last_name="Doe", email="John@gmail.com", gender="Male",
                                city='Paris', company="Ubisoft", title="CFO", lat=14.012655, lng=-31.012175)

        Customer.objects.create(id=2, first_name="Patrick", last_name="Starfish", email="patrick@gmail.com",
                                gender="Male", city='San Fransisco', company="Facebook",
                                title="This is patrick", lat=45.012655, lng=-11.012175)

    GRAPHQL_SCHEMA = schema

    def test_get_all_customers_query(self):
        response = self.query(
            '''
            query {
                customers {
                    id
                    firstName
                }
            }
            '''
        )
        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        self.assertEqual(len(content['data']['customers']), 2)
        self.assertEqual(content['data']['customers'][0]['firstName'], "John")

    def test_get_customer_by_id(self):
        response = self.query(
            '''
            query{
                customerSearch(id: 2){
                    id,
                    firstName
                }
            }
            ''',
        )
        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        self.assertEqual(content['data']['customerSearch']['firstName'], "Patrick")
