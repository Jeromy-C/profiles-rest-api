from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
	viewsets,
	status,
	filters,
	)
from rest_framework.authentication import TokenAuthentication

from . import serializers, models, permissions


class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializers.HelloSerializer
	
	def get(self, request, format = None):
		"""Returns a list of APIView features"""
		an_apiview = [
			'Uses HTTP methods as function (get, post, patch, put, delete)',
			'Is similar to a traditional Django View',
			'Gives you the most control over your application logic',
			'Is mapped amnually to URLs',
			]
		
		return Response({ 'message': 'Hello!', 'an_apiview': an_apiview })
	
	def post(self, request):
		"""Create a hello message with name"""
		serializer = self.serializer_class(data = request.data)
		
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}.'
			return Response({ 'message': message })
		else:
			return Response(
				serializer.errors,
				status.HTTP_400_BAD_REQUEST,
				)
	
	def put(self, req, pk = None):
		"""Handle updating an object"""
		return Response({ 'method': 'PUT' })
	
	def patch(self, req, pk = None):
		"""Handle a partial update of an object"""
		return Response({ 'method': 'PATCH' })
	
	def delete(self, req):
		"""Delete an object"""
		return Response({ 'method': 'DELETE' })

class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet"""
	
	serlializer_class = serializers.HelloSerializer
	
	def list(self, req):
		a_viewset = [
			'Uses actions (list, create, retrieve, update, partial_update)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code',
			]
		
		return Response({'message': 'Hello!', 'a_viewset':a_viewset})
	
	def create(self, req):
		"""Create a new hello message"""
		serializer = self.serlializer_class(data = req.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message':message})
		else:
			return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
		
	def retrieve(self, req, pk=None):
		return Response({'http_method': 'GET'})
	
	def update(self, req, pk=None):
		return Response({'http_method': 'PUT'})
	
	def partial_update(self, req, pk=None):
		return Response({'http_method': 'PATCH'})
	
	def destroy(self, req, pk=None):
		return Response({'http_method': 'DELETE'})
	
class UserProfileViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields =('name', 'email',)