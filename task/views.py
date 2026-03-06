from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer

# API ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """A professional DRF action to return user-specific task statistics."""
        tasks = self.get_queryset()
        total = tasks.count()
        completed = tasks.filter(status='Completed').count()
        pending = tasks.filter(status='Pending').count()
        
        # Additional statistics for a "professional" dashboard
        return Response({
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending,
            "completion_rate": round((completed / total * 100), 2) if total > 0 else 0
        })

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Task Created Successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Task Updated Successfully",
            "data": response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            "message": "Task Deleted Successfully"
        }, status=status.HTTP_200_OK)

# Template Views
def dashboard_page(request):
    """History and Stats View"""
    return render(request, 'task/dashboard.html', {'page_type': 'dashboard'})

def add_task_page(request):
    """Creation Page"""
    return render(request, 'task/add_task.html', {'page_type': 'dashboard'})
