from django.db import models

class Copier(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    total_counter = models.IntegerField()
    mono_counter = models.IntegerField()
    color_counter = models.IntegerField()

    ready = models.BooleanField(default=False)   # ✔ gotowa
    notes = models.TextField(blank=True)          # 📝 uwagi

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number})"
