
from django.contrib import admin
from django.urls import path
from medilabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index,name='index'),
    path('start/', views.start,name='start'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('', views.register,name='register'),
    path('login/', views.login,name='login'),

    path('contact/', views.contact,name='contact'),
    path('Patient/', views.Patient,name='Patient'),
    path('appointment/', views.Appoint,name='Appoint'),
    path('show/', views.show,name='show'),
    path('edit/<int:id>', views.delete),
    path('update/<int:id>', views.delete),
    path('delete/<int:id>', views.delete),

]