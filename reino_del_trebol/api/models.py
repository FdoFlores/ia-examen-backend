from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.crypto import get_random_string
from .utils import validate_names

class MagicAffinity(models.Model):
    magic_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'magic_affinity'

    def __str__(self) -> str:
        return f'{self.magic_name}'

class Mage(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=20, validators=[validate_names])
    last_name = models.CharField(max_length=20, validators=[validate_names])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    status = models.BooleanField(default=False)
    affinity = models.ForeignKey(MagicAffinity, on_delete=models.CASCADE, related_name='affinities')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_id()
        super().save(*args, **kwargs)

    def generate_id(self):
        return get_random_string(length=10)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
    
    class Meta:
        db_table = 'mage'