from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdministrator,IsStaff,IsStudent,IsTeacher
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

# Create your views here.
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Test(APIView):
    def get(self,request):
        print(request.auth)
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
            # login(request, user)
            # token, created = Token.objects.get_or_create(user=user)
            # if created:
            #     token.delete()  # Delete the token if it was already created
            #     token = Token.objects.create(user=user)
            # return Response({'token': token.key, 'username': user.username, 'role': user.role})
             # Create JWT token
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            # Optionally, include user role or other details
            return Response({
                'access': str(access_token),
                'refresh': str(refresh_token),
                'username': user.username,
                'role': user.role,
            })
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdministrator]

    def get(self,request):
        return Response({"message":"This is Admin View and accessible only by admin"})

class StaffView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsStaff]

    def get(self,request):
        return Response({"message":"This is Staff View and accessible only by admin"})

class TeacherView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsStaff]

    def get(self,request):
        return Response({"message":"This is Teacher View and accessible only by admin"})

class StudentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsStudent]

    def get(self,request):
        return Response({"message":"This is Student View and accessible only by admin"})