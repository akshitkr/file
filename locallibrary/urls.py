"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from catalog import views as catalog_views
from django.urls import re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first', catalog_views.index, name='index')

]


from django.urls import path
from django.contrib import admin

# Use include() to add URLS from the catalog application and authentication system
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
   

]


urlpatterns += [
   
    path('signup/', catalog_views.signup, name='signup'),
    path('first/', catalog_views.first, name='first'),
    path('welcome', catalog_views.welcome, name='welcome'),
    path('dashboard', catalog_views.profile, name='profile'),
    path('test', catalog_views.test, name='test'),


    
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add URL maps to redirect the base URL to our application




#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
