from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('<int:InspectionID>/detail/', views.detail, name='detail'),
    path('', views.home, name='home'),

]
