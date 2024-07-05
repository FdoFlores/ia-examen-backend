import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Mage, MagicAffinity, Grimoire

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def affinity():
    return MagicAffinity.objects.create(magic_name = "Agua")

@pytest.fixture
def mage(affinity):
    return Mage.objects.create(name = "Fernando", last_name = "Flores", age = 29, affinity = affinity)

@pytest.fixture
def grimoire():
    Grimoire.objects.create(grimoire_name = "Trebol de una hoja", weight = "0.40")
    Grimoire.objects.create(grimoire_name = "Trebol de dos hojas", weight = "0.30")
    Grimoire.objects.create(grimoire_name = "Trebol de tres hojas", weight = "0.15")
    Grimoire.objects.create(grimoire_name = "Trebol de cuatro hojas", weight = "0.10")
    Grimoire.objects.create(grimoire_name = "Trebol de cinco hojas", weight = "0.05")

@pytest.mark.django_db
def test_create_mage(api_client, affinity):
    url = reverse('create-solicitud')
    data = {'name' : 'Juan', 'last_name':'Perez', 'age':'33', 'affinity': affinity.id}
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Mage.objects.count() == 1
    assert Mage.objects.get().name == 'Juan'

@pytest.mark.django_db
def test_update_mage(api_client, affinity, mage):
    url = reverse('update-solicitud', args=[mage.id])
    updated_data = {'name' : 'Fernando', 'last_name':'Fierros', 'age':'29', 'affinity': affinity.id}

    response = api_client.put(url, updated_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    mage.refresh_from_db()
    assert mage.last_name == 'Fierros'

@pytest.mark.django_db
def test_update_mage_status(api_client, mage, grimoire):
    url = reverse('update-status', args=[mage.id])
    partial_update_data = {'status':'true'}

    response = api_client.patch(url, partial_update_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    mage.refresh_from_db()
    assert mage.grimoire_id is not None

@pytest.mark.django_db
def test_get_mage(api_client, mage):
    url = reverse('list-solicitudes')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert Mage.objects.all().first().name == 'Fernando'

@pytest.mark.django_db
def test_get_grimoires(api_client, mage, grimoire):
    url = reverse('list-asignaciones')

    grim = Grimoire.objects.all().first()
    mage.grimoire = grim
    mage.status = True
    mage.save()

    mages_with_grimoire = Mage.objects.select_related('grimoire').filter(grimoire__isnull=False)
    grimoires = Grimoire.objects.all()

    assert mages_with_grimoire[0].grimoire in grimoires

@pytest.mark.django_db
def test_delete_mage(api_client, mage):
    url = reverse('update-solicitud', args=[mage.id])
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Mage.objects.filter(id=mage.id).exists() is False