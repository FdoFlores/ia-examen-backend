from django.urls import path
from . import views

urlpatterns = [
    path('solicitud', views.MageCreateView.as_view()),
    path('solicitud/<str:pk>', views.MageUpdateView.as_view()),
    path('solicitud/<str:pk>/estatus', views.MageUpdateStatusView.as_view()),
    path('solicitudes', views.MageListView.as_view()),
    # get asignaciones
    path('solicitud/<str:pk>', views.MageDeleteView.as_view()),

    
]