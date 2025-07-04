from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Room
from myapp.api.serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
   routes =[
      'GET /api/',
      'GET /api/rooms',
      'GET /api/rooms/:id'
       
         # {'Endpoint': '/login/', 'method': 'POST', 'body': {'username': 'string', 'password': 'string'}, 'description': 'Login user'},
         #{'Endpoint': '/logout/', 'method': 'GET', 'description': 'Logout user'},
         #{'Endpoint': '/register/', 'method': 'POST', 'body': {'username': 'string', 'password1': 'string', 'password2': 'string'}, 'description': 'Register new user'},
         #{'Endpoint': '/rooms/', 'method': 'GET', 'description': 'Get list of rooms'},
         #{'Endpoint': '/room/<str:pk>/', 'method': 'GET', 'description': 'Get room details by ID'},
         #{'Endpoint': '/create-room/', 'method': 'POST', 'body': {'topic_id': 'int', 'name': 'string', 'description': 'string'}, 'description': 'Create a new room'},
         #{'Endpoint': '/update-room/<str:pk>/', 'method': 'PUT', 'body': {'topic_id': 'int', 'name': 'string', 'description': 'string'}, 'description': 'Update room details by ID'},
         #{'Endpoint': '/delete-room/<str:pk>/', 'method': 'DELETE',  description: "Delete room by ID"},
         #{'Endpoint':'/delete-message/<str:pk>/', method:'DELETE', description:'Delete message by ID'},
         #{'Endpoint':'/update_user/', method:'PUT', body:{'username':'string','email':'string'}, description:'Update user profile'},
         #{'Endpoint':'/topics/', method:'GET', description:'Get list of topics'},
         #{'Endpoint':'/activity/', method:'GET', description:'Get recent activity'}
         
   ]


   return Response(routes)

@api_view(['GET'])
def getRooms(request):
   rooms = Room.objects.all()
   serializer = RoomSerializer(rooms, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
   room = Room.objects.get(id=pk)
   serializer = RoomSerializer(room, many=False)
   return Response(serializer.data)



