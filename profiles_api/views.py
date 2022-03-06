from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from .serializers import HelloSerializer, ProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile

# Create your views here.
class HelloApiView(APIView):
    """Test api view"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns api view attributes"""
        an_apiview = [
            'Has Http Methods => get, post, put, patch, delete.',
            'It\'s similar to the traditional django view.',
            'Gives you the most controll over the application logic',
        ]

        return Response({'message': 'Successfully added an api view', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST    
            )

    def put(self, request, pk=None):
        """Updates an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partially updates an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test view set"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Returns a hello message and a viewset features."""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object using id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Update an object by its id"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partially update an object by its id"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Deletes an object by its id"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
