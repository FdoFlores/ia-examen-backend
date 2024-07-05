from django.core.management.base import BaseCommand
from api.models import Grimoire, MagicAffinity
from django.db import transaction

class Command(BaseCommand):
    help = 'This command seed the database tables Grimoire and Magic Affinity'

    def seed_grimoire(self):
        grimoires = {
            'Trebol de una hoja': '0.40',
            'Trebol de dos hojas': '0.30',
            'Trebol de tres hojas': '0.15',
            'Trebol de cuatro hojas': '0.10',
            'Trebol de cinco hojas': '0.05'
        }
        for key, value in grimoires.items():
            created = Grimoire.objects.create(grimoire_name = key, weight = value)
        
        print('Grimorios creados correctamente')

    def seed_affinity(self):

        affinities = ['Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra']

        for value in affinities:
            created = MagicAffinity.objects.create(magic_name = value)
        
        print('Afinidades magicas creadas correctamente')

    def handle(self, *args, **kwargs):
        self.seed_grimoire()
        self.seed_affinity()