from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('berita/', article, name="article"),
    path("berita/<slug:slug>/", article, name="detail"),
    path("anggota/", member, name="member")
]
