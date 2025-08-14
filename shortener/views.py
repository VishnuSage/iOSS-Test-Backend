
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortenURLView(APIView):
	def post(self, request):
		serializer = ShortURLSerializer(data=request.data)
		if serializer.is_valid():
			short_url = serializer.save()
			return Response({'short_code': short_url.short_code}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectView(APIView):
	def get(self, request, short_code):
		url_obj = get_object_or_404(ShortURL, short_code=short_code)
		return redirect(url_obj.original_url)
