from django.urls import path

from . import views

urlpatterns = [
    path('<int:InspectionID>/detail/', views.detail, name='detail'), # Detail URL
    path('', views.home, name='home'), # Home URL

]
