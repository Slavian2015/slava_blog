from django.shortcuts import render
from .models import Post, Profile


def posts_of_following_profiles(request):
    profile = Profile.objects.get(user=request.user)

    users = [user for user in profile.following.all()]
    posts = []

    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.post_set.all()
        posts.append(p_posts)

    my_posts = profile.profiles_posts()
    posts.append(my_posts)

    return render(request, 'home.html', {"profile": profile, "posts": posts})


def posts_of_my_profiles(request):
    profile = Profile.objects.get(user=request.user)
    posts = profile.profiles_posts()

    return render(request, 'home_all.html', {"profile": profile, "posts": posts})


def posts_of_all_profiles(request):
    posts = Post.objects.all()

    return render(request, 'home_all.html', {"posts": posts})