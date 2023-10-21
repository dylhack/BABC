from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("recommendations/", views.recommendations, name="recommendations"),
    path("submissions/", views.submissions, name="submissions"),
]
