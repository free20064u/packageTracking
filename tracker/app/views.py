from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import shipmentStatus, shipmentHistory
from .forms import shipmentStatusForm, updatePackageForm

from git import Repo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def updateWebsiteView(request):
    repo = Repo('/home/packageTracker/packageTracking')
    repo.remotes.origin.pull()
    return HttpResponse('pulled_success')


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
            messages.success(request, "Package retrieved successfully")
        except:
            messages.error(request, "No package found.")
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
            messages.success(request, 'Package added successfully')
            return redirect('addPackage')
        else:
            messages.error(request, 'Package not added')
            return render(request, 'app/addPackage.html', {'form':form})
    else:
        form = shipmentStatusForm()
        return render(request, 'app/addPackage.html', {'form': form})
    

def updatePackageView(request):
    if request.method == "POST":
        form = updatePackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Package updated successfully')
            return redirect('updatePackage')
        else:
            messages.error(request, 'Package not updated')
            return render(request, 'app/updatePackage.html', {'form':form})
    else:
        form = updatePackageForm()
        return render(request, 'app/updatePackage.html', {'form':form})