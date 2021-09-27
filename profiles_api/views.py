from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


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
				400,
				)

	def put(self, req, pk=None):
		"""Handle updating an object"""
		return Response({'method':'PUT'})
		
	def patch(self, req, pk=None):
		"""Handle a partial update of an object"""
		return Response({'method':'PATCH'})
		
	def delete(self, req):
		"""Delete an object"""
		return Response({'method':'DELETE'})