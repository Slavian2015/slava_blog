from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import blog.signals


