from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path('calculate_bmi/', views.calculate_bmi, name='calculate_bmi'),
    path('calculate_calories/', views.calculate_calories, name='calculate_calories'),
]
