from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('djoser.urls')),
    url(r'^', include('djoser.urls.jwt')),
]