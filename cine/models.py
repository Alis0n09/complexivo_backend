from django.db import models

class Show(models.Model):                                   # MARCA = SHOW
    movie_title = models.CharField(max_length=120, unique=True, null= False)
    room = models.CharField(max_length=120, null= False)
    price = models.DecimalField(
        max_digits=10,  # total de dígitos
        decimal_places=2,  # decimales
        default=0
    )
    available_seats = models.IntegerField(null=False)

    def __str__(self):
        return self.movie_title

class Reservation(models.Model):                             # VEHICULO = RESERVATION
    show = models.ForeignKey(Show, on_delete=models.PROTECT, related_name="reservations")
    customer_name  = models.CharField(max_length=120, null= False)
    seats = models.IntegerField(null= False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Status(models.TextChoices):
        RESERVED = "reservado", "Reservado"
        CONFIRMED = "confirmado", "Confirmado"
        CANCELLED = "cancelado", "Cancelado"

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.RESERVED
    )
    def __str__(self):
        return f"{self.show.movie_title} {self.customer_name} ({self.seats} {self.status} {self.created_at})"