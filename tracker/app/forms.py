from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import shipmentStatus, shipmentHistory


class shipmentStatusForm(forms.ModelForm):

    shippersFullname = forms.CharField(label='Shippers Fullname', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    shippersAddress = forms.CharField(label='Shippers Address', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    shippersPhone = forms.CharField(label='Shippers Phone', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    shippersEmail = forms.CharField(label='Shippers Email', max_length=100, widget= forms.EmailInput(attrs={'class': 'form-control'}))

    recieversFullname = forms.CharField(label='Recievers Fullname', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    recieversAddress = forms.CharField(label='Recievers Address', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    recieversPhone = forms.CharField(label='Recievers Phone', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    recieversEmail = forms.CharField(label='Recievers Email', max_length=100, widget= forms.EmailInput(attrs={'class': 'form-control'}))
    

    origin = forms.CharField(label='Origin', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    batch = forms.CharField(label='batch', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.CharField(label='status', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    destination = forms.CharField(label='destination', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # carrier = forms.CharField(label='carrier', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # typeOfSipment = forms.CharField(label='typeOfSipment', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # weight = forms.CharField(label='weight', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # carrierReferenceNo = forms.CharField(label='carrierReferenceNo', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # product = forms.CharField(label='product', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # paymentMethod = forms.CharField(label='paymentMethod', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    # quantity = forms.CharField(label='quantity', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    expectedDeliveryDate = forms.CharField(label='expectedDeliveryDate', max_length=100, widget= forms.DateInput(attrs={'class': 'form-control','type':'date'}))
    pickUpDate = forms.CharField(label='pickUpDate', max_length=100, widget= forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    



    class Meta:
        model = shipmentStatus
        fields = ['shippersFullname', 'shippersAddress', 'shippersPhone', 'shippersEmail', 'recieversFullname', 'recieversAddress', 'recieversPhone', 'recieversEmail', 'pickUpDate','expectedDeliveryDate','origin', 'batch', 'status', 'destination', 'carrierReferenceNo', 'product', 'quantity', 'paymentMethod','carrier', 'typeOfShipment', 'weight'
        #    
        ]


class updatePackageForm(forms.ModelForm):

    carrierReferenceNo = forms.CharField(label='Carrier Reference No', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Location', max_length=100, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = shipmentHistory
        fields = ['carrierReferenceNo', 'location']