from django.urls import path

from .views import posts_of_following_profiles, posts_of_my_profiles, posts_of_all_profiles
app_name = "posts"

urlpatterns = [
    path('', posts_of_my_profiles, name='home'),
    path('all/', posts_of_all_profiles, name='all_posts'),
    path('sub/', posts_of_following_profiles, name='sub_posts'),
]
