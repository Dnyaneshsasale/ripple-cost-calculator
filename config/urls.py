from django.contrib import admin
from django.urls import path
from core import views

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Core flow
    path('', views.landing, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('household/', views.household_profile, name='household_profile'),
    path('choices/', views.daily_choices, name='daily_choices'),
    path('results/', views.ripple_results, name='ripple_results'),
    
    # NEW FEATURES (add these)
   
    path('graph/', views.ripple_graph, name='ripple_graph'),
    path('map/', views.india_map, name='india_map'),
]
