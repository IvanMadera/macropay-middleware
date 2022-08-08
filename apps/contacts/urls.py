from django.urls import path
from apps.contacts.views import contact, contact_detail, contacts, error, ping

urlpatterns = [
    path('contacts/', contacts),
    path('contacts/<str:pk>/', contact_detail),
    path('contact/', contact),
]