from django.urls import path
from . import views
app_name='filmapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('film/<int:film_id>/',views.detail,name='detail'),
    path('add/',views.addMovie,name='addMovie'),
    path('edit/<int:id>/',views.editMovie,name='edit'),
    path('delete/<int:id>/', views.deleteMovie, name='delete'),

]