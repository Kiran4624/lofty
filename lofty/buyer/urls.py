from django.urls import path
from .views import *

urlpatterns = [
    path('', buyer_index_view, name='buyer_index_view'),
]