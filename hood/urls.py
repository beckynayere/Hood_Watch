from django.urls import path,include
from .  import views



urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood'),
]