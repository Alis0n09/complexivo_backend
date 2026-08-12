from rest_framework import serializers

class MovieCatalogSerializer(serializers.Serializer):                        # ServiceType = movie_catalog
    movie_title = serializers.CharField(max_length=120)
    genre = serializers.CharField(allow_blank=False)
    duration_min = serializers.IntegerField()
    rating  = serializers.CharField(max_length=120)
    is_active = serializers.BooleanField(default=True)

class EventType:
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    CHECKED_IN = "CHECKED_IN"

    CHOICES = [
        (CREATED, "Creado"),
        (CONFIRMED, "Confirmado"),
        (CANCELLED, "Cancelado"),
        (CHECKED_IN , "Chequeado"),

    ]

class Source:
    WEB = "WEB"
    MOBILE = "MOBILE"
    SYSTEM = "SYSTEM"

    CHOICES = [
        (WEB, "Web"),
        (MOBILE, "Mobile"),
        (SYSTEM, "System"),

    ]

class ReservationEventSerializer(serializers.Serializer):                      # VehicleService = reservation_events
    reservation_id = serializers.IntegerField()        # ID de Reservation (Postgres)
    event_type = serializers.ChoiceField(choices=EventType.CHOICES)                                                   
    source = serializers.ChoiceField(choices=Source.CHOICES)  
    note = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()