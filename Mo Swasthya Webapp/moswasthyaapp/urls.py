from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
  path('', views.landing, name="landing"),
  path('landing/<str:loc>', views.landinghosp, name="landinghosp"),
  path('show/<str:img>', views.show, name="show"),
  path('show/', views.showdefault, name="showdefault"),
  path('details/<str:id>', views.detailsection, name="detailsection"),
  
]