from django.urls import path
from . import views

urlpatterns = [
    path('solicitud', views.MageCreateView.as_view(), name='create-solicitud'),
    path('solicitud/<str:pk>', views.MageUpdateView.as_view(), name='update-solicitud'),
    path('solicitud/<str:pk>/estatus', views.MageUpdateStatusView.as_view(), name='update-status'),
    path('solicitudes', views.MageListView.as_view(), name='list-solicitudes'),
    path('asignaciones', views.GrimoireListView.as_view(), name='list-asignaciones'),
]