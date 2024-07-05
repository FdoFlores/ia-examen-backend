from django.shortcuts import render
from api.models import Mage

# Create your views here.
def index(request):
    mages = Mage.objects.all()
    print(mages)
    return render(request, 'front/index.html', context={ 'mages': mages })