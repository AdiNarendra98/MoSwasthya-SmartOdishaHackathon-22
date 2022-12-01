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
  path('detailsodia/<str:id>', views.detailsectionodia, name="detailsectionodia"),
  path('scheme', views.scheme, name="scheme"),
  path('bsky', views.bsky, name="bsky"),
  path('bskyodia', views.bskyodia, name="bskyodia"),
  path('ostf', views.ostf, name="ostf"),
  path('ostfodia', views.ostfodia, name="ostfodia"),
  path('niramaya', views.niramaya, name="niramaya"),
  path('niramayaodia', views.niramayaodia, name="niramayaodia"),
  path('prediction', views.prediction, name="prediction"),
  path('predictionodia', views.predictionodia, name="predictionodia"),
  path('schemeodia', views.schemeodia, name="schemeodia"),
  path('tableu', views.tableu, name="tableu"),
  path('tableuodia', views.tableuodia, name="tableuodia"),
  path('landingodia', views.landingodia, name="landingodia"),
  path('landingodia/<str:loc>', views.landinghospodia, name="landinghospodia"),
  path('pred_disease', views.pred_disease, name="pred_disease"),
  path('pred_disease_odia', views.pred_disease_odia, name="pred_disease_odia"),
  
]