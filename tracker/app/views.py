from django.shortcuts import render
from .models import shipmentStatus, shipmentHistory

# Create your views here.
def homeView(request):
    return render(request, 'app/index.html')


def aboutView(request):
    return render(request, 'app/about.html')


def servicesView(request):
    return render(request, 'app/services.html')


def trackingView(request):
    if request.method == "POST":
        code = (request.POST.get('trackingCode'))
        packageInfo = shipmentStatus.objects.get(carrierReferenceNo = code)
        try:
            packageHistory = shipmentHistory.objects.filter(carrierReferenceNo = code)
            print(packageHistory)
        except:
            packageHistory=None
            
        

        return render(request, 'app/tracking-detail.html', {'packageInfo':packageInfo, 'packageHistory': packageHistory})
    else:
        return render(request, 'app/tracking.html')


def contactView(request):
    return render(request, 'app/contact.html')


def getaquoteView(request):
    return render(request, 'app/get-a-quote.html')
