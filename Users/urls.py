from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Users import views

app_name='Users'

urlpatterns = [

    path('',views.HomeView.as_view(),name='Home'),
]