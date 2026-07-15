from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.shortcuts import get_object_or_404
from .models import Restaurant
from .serializers import RestaurantSerializer

# --- Session 3: ModelViewSet with Pagination, Filtering, and Ordering ---

class RestaurantPageNumberPagination(PageNumberPagination):
    page_size = 3

class RestaurantLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for Restaurant.
    Handles GET (list/detail), POST, PUT, PATCH, DELETE automatically.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    # Switch pagination to LimitOffsetPagination as per requirement 3.
    # To use PageNumberPagination (requirement 2), uncomment the line below instead.
    # pagination_class = RestaurantPageNumberPagination
    pagination_class = RestaurantLimitOffsetPagination
    
    # Requirement 4 & 5: Filtering and Ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['cuisine']
    ordering_fields = ['name', 'cuisine']

# --- Approach 1: Using APIView ---

class RestaurantListCreateAPIView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Approach 2: Refactored Using GenericAPIView and Mixins ---

class RestaurantGenericListCreateView(mixins.ListModelMixin,
                                      mixins.CreateModelMixin,
                                      generics.GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RestaurantGenericDetailView(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  generics.GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
