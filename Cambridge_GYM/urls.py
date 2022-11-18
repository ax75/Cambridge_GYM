"""Cambridge_GYM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from BaseApp import views as baseApp_views
from SessionManager import views as sess_views

urlpatterns = [
    path('accounts/login/', baseApp_views.user_login_view, name="login"),
    path('accounts/login/validate/', baseApp_views.validate_login, name="validate_login"),
    path('admin/', admin.site.urls),
    path('', sess_views.home, name="home"),
    path('select-date/', sess_views.select_date, name="select_date"),
    path('select-slot/', sess_views.select_slot, name="select_slot"),
    path('slot-details/<str:date>', sess_views.confirm_slot_view, name="confirm_slot_view"),
    path('book-slot/<str:date>', sess_views.book_slot, name="book_slot"),
    path('list-booked-slots/', sess_views.view_booked_slots, name="list_booked_slots"),
    
    
    path('accounts/logout/', baseApp_views.user_logout, name="logout"),
]
