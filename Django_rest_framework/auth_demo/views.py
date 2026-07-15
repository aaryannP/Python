from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Playlist, Order, CartItem, Ticket
from .serializers import PlaylistSerializer, OrderSerializer, CartItemSerializer, TicketSerializer
from .permissions import IsPremiumUser

# 1. BasicAuthentication for /api/playlists/
class PlaylistAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

# 2. TokenAuthentication for /api/orders/
class OrderAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

# 3. SessionAuthentication for /api/cart/
class CartAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 4. Custom permission IsPremiumUser for /api/tickets/
class TicketAPIView(APIView):
    # Depending on setup, you might want to specify an authentication_class as well, 
    # but we'll stick to permissions as per the requirement.
    permission_classes = [IsAuthenticated, IsPremiumUser]

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
