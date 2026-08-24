from django.urls import path
from newapp import views
urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('stock/',views.stock,name='stock'),
    path('add_stock/',views.add_stock,name='add_stock'),
    path('reports/',views.reports,name='reports'),



]