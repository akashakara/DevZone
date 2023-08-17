from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    # ex: /projects/
    path('', views.index, name='index'),
    # ex: /projects/3/
    path('<int:project_id>/', views.detail, name='detail'),
    # ex: /projects/3/members/
    path('<int:project_id>/members/', views.members, name='members'),
    # ex: /projects/3/partake/
    path('<int:project_id>/partake/', views.partake, name='partake'),
]