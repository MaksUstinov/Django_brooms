from django.urls import path
from .views import suppliers, town


urlpatterns = [
    path('', suppliers),
    path('<int:town>/', town, name='town'),
]