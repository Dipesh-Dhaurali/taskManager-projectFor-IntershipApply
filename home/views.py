from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

# API Views
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User Created Successfully",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Template Views
def landing_page(request):
    return render(request, 'home/landing.html', {'page_type': 'landing'})

def login_page(request):
    return render(request, 'home/login.html', {'page_type': 'auth'})

def register_page(request):
    return render(request, 'home/register.html', {'page_type': 'auth'})
