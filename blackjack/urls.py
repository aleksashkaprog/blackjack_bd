from django.urls import path
from django.views.generic import TemplateView
from .views import BJEditFormView, BJFormView, QRView

from . import views

urlpatterns = [
    path('', views.bd_list, name='bd_list'),
    path('blackjack/create/', BJFormView.as_view()),
    path('blackjack/<int:profile_id>/edit/', BJEditFormView.as_view()),
    path('blackjack/<int:profile_id>/qrcode/', QRView.as_view())

]