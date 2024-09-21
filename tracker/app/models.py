from time import timezone
from django.db import models

# Create your models here.
class shipmentStatus(models.Model):
    shippersFullname = models.CharField(max_length=200)
    shippersAddress = models.CharField(max_length=200, default='')
    shippersPhone = models.CharField(max_length=15)
    shippersEmail = models.EmailField()

    recieversFullname = models.CharField(max_length=200)
    recieversAddress = models.CharField(max_length=200, default='')
    recieversPhone = models.CharField(max_length=15)
    recieversEmail = models.EmailField()

    receivedDate = models.DateField(auto_now_add=True)
    origin = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    typeOfShipment = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    carrierReferenceNo = models.CharField(max_length=100, default='')
    product = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    paymentMethod = models.CharField(max_length=100)
    expectedDeliveryDate = models.DateField()
    pickUpDate = models.DateField()

    def createCarrieReferenceNo(self):
        self.carrierReferenceNo = "wewe23123241fefef"
        return self.carrierReferenceNo
    

    def getCarrierReferenceNo(self):
        return self.carrierReferenceNo
        
    def __init(self):
        self.createCarrieReferenceNo()


    def __str__(self):
        return self.product



class shipmentHistory(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    updatedBy = models.CharField(max_length=100, default="admin")
    carrierReferenceNo = models.CharField(max_length=100,default='')

   


