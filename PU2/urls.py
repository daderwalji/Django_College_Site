"""final URL Configuration

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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from dash import views as dash_views
from results import views as results_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(template_name='clg/home.html'), name='logout'),
    path('admin-profile/', dash_views.teacher_profile, name='admin-profile'),
    path('admin-login/',auth_views.LoginView.as_view(template_name='dash/login.html'), name='admin-login'),
    path('admin-logout/',auth_views.LogoutView.as_view(template_name='clg/home.html'), name='admin-logout'),
    path('student-form/', results_views.resultform, name='student-form'),
    path('student-result/', results_views.studentresult, name='student-result'),
    path('', include('clg.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

