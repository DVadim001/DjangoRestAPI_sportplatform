from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Equipment(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    quantity = models.PositiveIntegerField("Количество")
    is_available = models.BooleanField("Доступно", default=True)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентарь"


class EquipmentReservation(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} reserved {self.equipment} for {self.event} from {self.start_date} to {self.end_date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.equipment.is_available:
            self.equipment.is_available = False  # теперь булево
            self.equipment.save()
