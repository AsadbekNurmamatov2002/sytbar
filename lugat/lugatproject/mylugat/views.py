from django.shortcuts import render
from .models import Lugat, English

# Create your views here.
def home(request):
    english=English.objects.all()
    return render(request, "home.html", {"english":english})
def Index(request):
    # lugat=Lugat.objects.all()
    soz=request.GET.get("q", "")
    if soz and soz!="":
        natija=Lugat.objects.filter(inglizcha__contains=soz).all()
    else:
        natija=None
    context={
        "q": soz,
        "natija":natija
    }
    return render(request, "index.html", context)
