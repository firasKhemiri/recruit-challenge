from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from recruit_challenge.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),

    # Path to the GraphQL schema.
    path('graphql/', csrf_exempt(GraphQLView.as_view(schema=schema))),

    # Path to the templates that will consume the API.
    url('', include('core.urls')),
]
