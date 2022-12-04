from django.urls import path
from .views import SeasonListView


urlpatterns = [
    path('seasonStatus/',SeasonListView.as_view(),name='order_seasons_status')
]