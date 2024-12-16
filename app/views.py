from django.shortcuts import redirect, render
from django.contrib import messages
from .models import shipmentStatus, shipmentHistory
from .forms import shipmentStatusForm, updatePackageForm

from django.http import HttpResponse
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
            packageHistory = shipmentHistory.objects.filter(carrierReferenceNo = code).order_by('-date','-time')
            #print(list(packageHistory.values_list('latitude','longitude')))
        except:
            packageHistory=None
        latlngs=[]
        for latlng in list(packageHistory.values_list('latitude','longitude')):
            items=[]
            for item in latlng:
                items.append(float(item))
            latlngs.append(items)
   
        context =  {
            'packageInfo':packageInfo, 
            'packageHistory': packageHistory,
            'packageHistoryValues': list(packageHistory.values('location','latitude','longitude','currentLocation')),
            'latlngs':latlngs,
            }

        return render(request, 'app/tracking-detail.html',context)
    else:
        return render(request, 'app/tracking.html')


def contactView(request):
    return render(request, 'app/contact.html')


def getaquoteView(request):
    return render(request, 'app/get-a-quote.html')


def dashboardView(request):
    packages = shipmentStatus.objects.all()
    context = {
        'packages':packages,
    }
    if request.method=='POST':
        pass
    else:
        return render(request, 'app/dashboard.html', context)

def updateCurrentLocationView(request):
    if request.method == 'POST':
        package_reference = request.POST['referenceId']
        packageLocations = shipmentHistory.objects.filter(carrierReferenceNo=package_reference)
        print(packageLocations)
        context = {
            'packageLocations': packageLocations,
        }
        return render(request, 'app/packageLocations.html', context)
    
def updateCurrentLocationChangeView(request, id=None):
    if request.method == 'POST':
        package_reference = request.POST['referenceId']
        packageLocations = shipmentHistory.objects.filter(carrierReferenceNo=package_reference)
        for package in packageLocations:
            if package.id == id:
                package.currentLocation = True
                package.save()
            else:
                package.currentLocation = False
                package.save()
            print(package.id, id)
        return redirect('dashboard')


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