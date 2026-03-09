from django.urls import path
from . import views
from .views import CourseListViews

urlpatterns = [
    path('', views.courses),
    path('show_date/', views.show_current_date),
    path('get_path/', views.get_path),
    path('get_props/', views.get_http_params),
    path('courses/',CourseListViews.as_view(),name="all courses"),
    path('<str:name>/', views.get_course),
]