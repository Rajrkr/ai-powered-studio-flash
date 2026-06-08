"""
URL configuration for studioflash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from mainapp.views import home, services,register,forgot_password
from mainapp.views import home, services, register, forgot_password, booking
from mainapp.views import delete_booking
from mainapp.views import booking_history, predict_price
from mainapp.views import recommend_package,dashboard,profile,logout,services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('services/', services),
    path('register/', register),
    path('forgot/', forgot_password),
    

    path('booking/', booking),
    path('history/', booking_history),
    path('delete/<int:id>/', delete_booking),
    path('predict-price/', predict_price),
    path('recommend-package/', recommend_package),
    path('dashboard/', dashboard),
    path('profile/', profile),
    path('logout/', logout),
     path('services/', services),

]