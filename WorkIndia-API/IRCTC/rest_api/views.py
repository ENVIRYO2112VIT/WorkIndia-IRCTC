from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from irctcBase.models import User, Train
from .serializers import UserSerializer, TrainSerializer, TrainSearchSerializer


class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        print(username, email)
        if (email.find('@') == -1):
            return Response({'status': 'Please Enter Your Valid Email ID', 'status_code':404}, status=404)
        else:
            user_exists = User.objects.filter(email=email).exists()
            if (user_exists == True):
                return Response({'status': 'User with the given Email ID already exists', 'status_code':404}, status=404)
            username_exists = User.objects.filter(username=username).exists()
            if (username_exists == True):
                return Response({'status': 'Username exists already', 'status_code':404}, status=404)
            print("Hello")
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'errors': 'Email or Username Already Exists', 'status_code':404}, status=404)
            serializer.save()
            return Response({'status': "Account successfully created", 'status_code': 200}, status=200)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        print(user)
        if user is None:
            return Response({"status": "Incorrect username/password provided. Please retry", "status_code": 401})
                # raise AuthenticationFailed('User Not Found!')

        if not user.password == password:
            return Response({"status": "Incorrect username/password provided. Please retry", "status_code": 401})
            # raise AuthenticationFailed('Password is Incorrect!')

        refresh = RefreshToken.for_user(user)
        return Response({'status':"Login successful", 'status_code': 200, 'access_token': str(refresh.access_token), 'refresh_token': str(refresh)}, status=200)


class TrainView(APIView):
    def post(self, request):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Train added successfully", "train_id": ""})
        
        return Response({'errors': 'Serializer Failed', 'status_code':404}, status=404)

class TrainFetchView(APIView):
    def get(self, request):
        source = self.request.query_params.get('source','')
        destination = self.request.query_params.get('destination','')
        # destination = request.data['destination']
        train_av = Train.objects.filter(source = source, destination = destination)
        serializer = TrainSearchSerializer(train_av, many=True)
        return Response(serializer.data, status = 200)