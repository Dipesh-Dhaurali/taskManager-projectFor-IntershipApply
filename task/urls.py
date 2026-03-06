from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, dashboard_page, add_task_page

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Template URLs
    path('dashboard/', dashboard_page, name='dashboard'),
    path('add-task/', add_task_page, name='add_task_page'),

    # API URLs
    path('api/', include(router.urls)),
]
