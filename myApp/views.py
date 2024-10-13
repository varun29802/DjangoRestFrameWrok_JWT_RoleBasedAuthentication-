from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .permissions import isAdministrator,isStaff,isTeacher,isStudent

# Create your views here.
class Test(APIView):
    def get(self,request):
        return Response({"message":"You are calling test Api"})
 
class UserRegister(APIView):
    def post(self,request):
        try:
            print(1)
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({"data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)})

class UserLoginView(ObtainAuthToken):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the token key from the request
            token_key = request.auth.key
            
            # Try to retrieve the token
            token = Token.objects.get(key=token_key)
            token.delete()

            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)        
        except Token.DoesNotExist:
            raise NotFound({'detail': 'Token not found.'})
        except Exception as e:
            # Handle any other exceptions
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class AdminView(APIView):
    permission_classes = [IsAuthenticated,isAdministrator]

    def get(self,request):
        return Response({"message":"This is Admin View and accessible only by admin"})

class StaffView(APIView):
    permission_classes = [IsAuthenticated,isStaff]

    def get(self,request):
        return Response({"message":"This is Staff View and accessible only by admin"})

class TeacherView(APIView):
    permission_classes = [IsAuthenticated,isTeacher]

    def get(self,request):
        return Response({"message":"This is Teacher View and accessible only by admin"})

class StudentView(APIView):
    permission_classes = [IsAuthenticated,isStudent]

    def get(self,request):
        return Response({"message":"This is Student View and accessible only by admin"})