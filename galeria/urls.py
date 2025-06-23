from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("imagem/<int:image_id>/", views.image, name="imagem"),
]