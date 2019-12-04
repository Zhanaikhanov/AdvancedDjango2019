from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import MainUser
from api.serializers.auth import UserSerializer


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data.get('user')
        token, created = Token.objects.get_or_create(user=user)
        User = MainUser.objects.get(username=user)
        serialized = UserSerializer(User, many=False)
        return Response({'code': 0, 'token': token.key, 'user': serialized.data}, status=status.HTTP_200_OK)
    else:
        return Response({'code': 1}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"code": 0}, status=status.HTTP_201_CREATED)
    else:
        return Response({"code": 1, "error": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

