import random
from .models import Grimoire

class GrimoireAssigner:
    def __init__(self) -> None:
        pass

    def get_names_weights(self):
        weights = Grimoire.objects.values_list('weight', flat=True)
        names = Grimoire.objects.values_list('grimoire_name', flat=True)

        names_l = [name for name in names]
        weights_l = [float(weight) for weight in weights]

        return names_l, weights_l

    def assign(self, names, weights):
        random_grim = random.choices(names, weights, k=1)[0]
        random_grim = Grimoire.objects.filter(grimoire_name = random_grim).first()
        return random_grim