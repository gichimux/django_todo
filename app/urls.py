from django.urls import path
from . import views
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'add_goal/', views.add_goal, name='add_goal'),
    path(r'goal_detail/<int:id>/', views.goal_detail, name='goal_detail'),
    path(r'<int:id>/edit/', views.goal_update, name='update'),
    path(r'goals/<int:id>/delete/', views.goal_delete, name='delete'),
]
