from django.db import models

# Create your models here.
class add_stock(models.Model):
    unitchoices= [
    ("Tablet", "Tablet"),
    ("Capsule", "Capsule"),
    ("Syrup", "Syrup"),
    ("Suspension", "Suspension"),
    ("Injection", "Injection"),
    ("Cream", "Cream"),
    ("Ointment", "Ointment"),
    ("Gel", "Gel"),
    ("Lotion", "Lotion"),
    ("Drops", "Drops"),
    ("Spray", "Spray"),
    ("Inhaler", "Inhaler"),
    ("Powder", "Powder"),
    ("Sachet", "Sachet"),
    ("Granules", "Granules"),
    ("Mouthwash", "Mouthwash"),
    ("Gargle", "Gargle"),
    ("Solution", "Solution"),
    ("Emulsion", "Emulsion"),
    ("Infusion", "Infusion"),
    ("Patch", "Patch"),
    ("Suppository", "Suppository"),
    ("Shampoo", "Shampoo"),
    ("Soap", "Soap"),
    ("Other", "Other"),
]
    
    status_choice=[
        ('In stock','In stock'),
        ('Out of stock','Out of Stock'),
        ('Low Stock','Los Stock'),
    ]
       
   
    medicineid=models.CharField(max_length=50)
    invoice=models.CharField(max_length=100)
    medicinename=models.CharField(max_length=50)
    batchno=models.CharField(max_length=100)
    currentstock = models.IntegerField()
    newstock = models.IntegerField()
    
    unit=models.CharField(max_length=100,choices= unitchoices)
    unitprice=models.DecimalField(max_digits=20,decimal_places=2)
    
    totalamount=models.DecimalField(max_digits=12, decimal_places=2)
    purchasedate=models.DateField()
    supplier=models.CharField(max_length=50)
    expiredate=models.DateField()
    status=models.CharField(max_length=30,choices=status_choice)
    lastupdate=models.DateField()
    remark=models.TextField(max_length=500)

    def __str__(self):
        return self.name


class out_stock(models.Model):
    
  
   
    medicineid=models.CharField(max_length=100)
    invoice=models.CharField(max_length=100)    
    medicinename=models.CharField(max_length=100)
    batchno=models.CharField(max_length=100)
    currentstock=models.CharField(max_length=100)
    unit=models.CharField(max_length=100)
    unitprice=models.CharField(max_length=100)
    outstock=models.CharField(max_length=100)
    totalamount=models.DecimalField(max_digits=12, decimal_places=2)
    date=models.DateField()
    customername=models.CharField(max_length=100)
    expiredate=models.DateField()
    status=models.CharField(max_length=100)
    lastdate=models.DateField()
    remark=models.TextField(max_length=500)


    def __str__(self):
        return self.name




