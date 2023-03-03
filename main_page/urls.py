from django.urls import path
from .views import main, search
from . import views

urlpatterns = [
    path('', main, name='main_page'),
    path('search', search, name='search'),
    path('<int:id>', views.detail_page, name='detail'),
]
