from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import BookingSerializer, ListSerializer
from datetime import datetime

class FlightsListAPIView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

class BookingsListAPIView(ListAPIView):
    today = datetime.today()
    queryset = Booking.objects.all().filter(date__gt=today)
    serializer_class = BookingSerializer
    