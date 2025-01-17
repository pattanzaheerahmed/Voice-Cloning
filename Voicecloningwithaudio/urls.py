"""
URL configuration for VoiceCloningWithAudio project.

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
from django.conf import settings
from django.conf.urls.static import static
from UserApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),
    path('LogAction', views.LogAction),
    path('register', views.register),
    path('RegAction', views.RegAction),
    path('Upload', views.Upload),
    path('AudioUpAction', views.AudioUpAction),
    path('Text', views.Text),
    path('TextAction', views.TextAction),
    path('home', views.home),
    path('Listen', views.Listen),
    path('listenaudio', views.listenaudio),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
