"""Add models to the admin dashboard."""
from django.contrib import admin
from core.models import Customer

admin.site.register(Customer)
