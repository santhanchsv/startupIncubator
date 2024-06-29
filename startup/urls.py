"""startup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls')),
    path('accounts/' , include('accounts.urls')),
    path('socialaccounts/' , include('allauth.urls')),
    
  
    path('chat/', chat_views.home, name='home'),
    path('<str:room>/', chat_views.room, name='room'),
    path('checkview', chat_views.checkview, name='checkview'),
    path('send', chat_views.send, name='send'),
    path('getMessages/<str:room>/', chat_views.getMessages, name='getMessages'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

