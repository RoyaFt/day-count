from django.urls import path
from . import views


urlpatterns = [
    path ('<int:day>/',views.index3),
    path ('<str:day>/',views.index2, name='day-of-week'),
    path ('',views.index4),
    
]