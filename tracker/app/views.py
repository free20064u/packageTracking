from django.shortcuts import redirect, render
from .models import shipmentStatus, shipmentHistory
from .forms import shipmentStatusForm, updatePackageForm

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
        try:
            packageInfo = shipmentStatus.objects.get(carrierReferenceNo = code)
        except:
            return redirect('tracking')
        try:
            packageHistory = shipmentHistory.objects.filter(carrierReferenceNo = code)
        except:
            packageHistory=None
            
        

        return render(request, 'app/tracking-detail.html', {'packageInfo':packageInfo, 'packageHistory': packageHistory})
    else:
        return render(request, 'app/tracking.html')


def contactView(request):
    return render(request, 'app/contact.html')


def getaquoteView(request):
    return render(request, 'app/get-a-quote.html')


def dashboardView(request):
    return render(request, 'app/dashboard.html')

def addPackageView(request):
    if request.method == "POST":
        form = shipmentStatusForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('addPackage')
        else:
            return render(request, 'app/addPackage.html', {'form':form})
    else:
        form = shipmentStatusForm()
        return render(request, 'app/addPackage.html', {'form': form})
    

def updatePackageView(request):
    if request.method == "POST":
        form = updatePackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('updatePackage')
        else:
            return render(request, 'app/updatePackage.html', {'form':form})
    else:
        form = updatePackageForm()
        return render(request, 'app/updatePackage.html', {'form':form})