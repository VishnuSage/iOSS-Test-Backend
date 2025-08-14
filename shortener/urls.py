from django.urls import path
from .views import ShortenURLView, RedirectView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:short_code>/', RedirectView.as_view(), name='redirect-url'),
]
