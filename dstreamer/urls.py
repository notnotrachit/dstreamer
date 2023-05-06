"""
URL configuration for dstreamer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from streamer import views as streamer_views
from django.urls import re_path
from dstreamer import consumer
from streamer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', streamer_views.index, name='index'),
    # re_path(r'^ws/stream/$', consumer.StreamConsumer.as_asgi()),
    # Streaming URL
    path('stream/<str:stream_id>/', views.stream, name='stream'),
    path('ws/stream/<str:stream_id>/', consumer.StreamConsumer.as_asgi()),
    
    # Viewing URL
    path('ws/watch/<str:stream_id>/', views.watch, name='watch'),
    path('new_room/', views.new_room, name='new_room'),
    path('join_room/', views.join_room, name='join_room'),
]
