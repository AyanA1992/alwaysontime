from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('salats/', views.salat_index, name='index'),
    path('salats/<int:salats_id>/', views.SalatDetail.as_view(), name='detail'),
    path('salats/create/', views.SalatCreate.as_view(), name='salats_create'),
    path('salats/<int:pk>/update/', views.SalatUpdate.as_view(), name='salats_update'),
    path('salats/<int:pk>/delete/', views.SalatDelete.as_view(), name='salats_delete'),
    # path('salats/<int:salat_id>/add_salat/', views.add_salat, name='add_prayers'),
    # path('salats/<int:salat_id>/add_photo/', views.add_photo, name='add_photo'),
    path('salats/<int:salats_id>/assoc_prayers/<int:prayers_id>/', views.assoc_prayers, name='assoc_prayers'),
    path('prayers/create/', views.PrayerCreate.as_view(), name='prayers_create'),
    path('prayers/', views.PrayerIndex.as_view(), name='prayers_index'),
    path('prayers/<int:pk>/', views.PrayersDetail.as_view(), name='prayers_detail'),
    path('prayers/<int:pk>/update/', views.PrayerUpdate.as_view(), name='prayers_update'),
    path('prayers/<int:pk>/delete/', views.PrayerDelete.as_view(), name='prayers_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]