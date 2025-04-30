from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class RoomType(models.Model):
    roomType = models.CharField(max_length=50, unique=True)  # Example: "Single", "Double", "Suite"
    name = models.CharField(max_length=100)  # Example: "Standard Suite", "Family Room"
    description = models.TextField(blank=True, null=True)
    capacity = models.PositiveIntegerField()  # number of guests

    def __str__(self):
        return f"{self.name} ({self.roomType})"
    

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ForeignKey('RoomType', on_delete=models.PROTECT, related_name='rooms')
    number = models.CharField(max_length=10, unique=True)  # Room number, unique per room
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)  # Example: 150.00
    available = models.BooleanField(default=True)  # True if the room is available for booking
    services = services = models.ManyToManyField(Service, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel.name} - Room {self.number} ({self.room_type.name})"

