from django.urls import path
from .views import home_view, Portfolio_View

urlpatterns = [
    path('', home_view, name='index'),
    path('<int:pk>/', Portfolio_View.as_view(), name='portfolio')
]