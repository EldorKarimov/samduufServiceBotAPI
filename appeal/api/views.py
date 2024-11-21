from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from appeal.models import *
from .serializers import *

class RequestedUserCreateView(APIView):
    def get(self, request):
        appeal_lps = RequestedUser.objects.all()
        serializer = RequestedUserSerializer(appeal_lps, many = True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = RequestedUserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RequestedUserMessageCreateAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        serializer = RequestedUserMessageSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)