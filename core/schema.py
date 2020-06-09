"""This module contains the GraphQL API endpoint and its queries."""
import graphene
from graphene_django import DjangoObjectType

from .models import Customer


class CustomerType(DjangoObjectType):

    class Meta:
        model = Customer


class Query(graphene.ObjectType):
    customers = graphene.List(CustomerType)

    customer_search = graphene.Field(CustomerType, id=graphene.Int())

    def resolve_customers(self, info, **kwargs):
        """ Get all customers."""
        return Customer.objects.all()

    def resolve_customer_search(self, info, **kwargs):
        """ Get a single customer by its id."""
        customer_id = kwargs.get("id", 0)

        if customer_id is not None:
            return Customer.objects.get(pk=customer_id)
