from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login


#Register User API 
class RegisterAPI(APIView):

    """
    User register api
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        username =request.data.get('username')
        password =request.data.get('password')
        if username and password:
            try:
                user_name = User.objects.get(username=username)
            except ObjectDoesNotExist as e:
                user_name =None
            if not user_name:
                    new_user =User.objects.create(username=username, password=make_password(password))
                    return Response(data=[{"message":"You have been registered successfully"}] ,status=status.HTTP_200_OK)

            else:
                return Response(data=[{"message":"This user is already registred"}],status=status.HTTP_400_BAD_REQUEST)
        else:
        	return Response(data=[{"message":"Please provide username and password"}],status=status.HTTP_400_BAD_REQUEST)
             

# User Login API
class UserLogin(APIView):
    """
    Api to login user
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            try:
                userobj = User.objects.get(username = username)
            except ObjectDoesNotExist as e:
                userobj =None
            if userobj:
                    user = authenticate(username=userobj.username, password=password)
                    login(request,user)
                    if user:
                        token, is_created = Token.objects.get_or_create(user=user)
                        return Response(data=[{"token":token.key    ,"message":"login successfully"}],status=status.HTTP_200_OK)
                    else:
                        return Response(data=[{"message":"username password combination failed"}],status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(data=[{"message":"username password combination failed"}],status=status.HTTP_400_BAD_REQUEST)
        else:
                return Response(data=[{"message":"Bad request"}],status=status.HTTP_400_BAD_REQUEST)



