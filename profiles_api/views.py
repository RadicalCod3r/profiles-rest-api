from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

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