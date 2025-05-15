from django.db import models
from vehicles.models import Vehicle

# Create your models here.
class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Número da Vaga'
    )

    is_occupied = models.BooleanField(
        default=False,
        verbose_name='Ocupado'
    )

    created_at = models.DateTimeField( 
        auto_now_add=True,
        verbose_name="Criado em"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"
        ordering = ["created_at"]

        
    def __str__(self):
        return f"{self.spot_number}" 


class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='parking_records',
        verbose_name='Veículo'
    )

    parking_sport = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='parking_records',
        verbose_name='Vaga'
    )

    entry_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Horário de Entrada'
    )

    exit_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Horário de Saída'
    )

    created_at = models.DateTimeField( 
        auto_now_add=True,
        verbose_name="Criado em"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    class Meta:
        verbose_name = "Registo"
        verbose_name_plural = "Rigistos"
        ordering = ["created_at"]

        
    def __str__(self):
        return f"{self.vehicle} - {self.parking_sport} - {self.entry_time}" 