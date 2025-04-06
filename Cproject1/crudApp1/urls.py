from django.urls import path
from .import views

urlpatterns = [
    path('vv/', views.votersView, name='add_url'),
    path('/', views.displayInfo, name='show_url'),
    path('uv/<int:pk>', views.updateInfo, name='upd_url'),
    path('dv/<int:pk>', views.deleteInfo, name='del_url')
]
