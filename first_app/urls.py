from django.urls import path
from first_app.views import first_view

urlpatterns = [
    path('', first_view),
]