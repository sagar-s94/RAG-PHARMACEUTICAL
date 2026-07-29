from django.db import models
# from medicine.models import allopathy
# Create your models here.
 
class allopathy_medicine(models.Model):
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
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=unitchoices)
    company=models.CharField(max_length=100)
    quantity=models.IntegerField()
    packing_size=models.CharField(max_length=50)
    
    price=models.DecimalField(max_digits=10, decimal_places=2)
    expirydate=models.DateField()
    

    class Meta:
        managed=True
        db_table= "allopathy_medicine"

    def __str__(self):
        return self.name
    




class ayurvedic_medicine(models.Model):
    
    
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    quantity=models.IntegerField()
    packing_size=models.CharField(max_length=50,)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    expirydate=models.DateField()
    

    class Meta:
        managed=True
        db_table= "ayurvedic_medicine"

    def __str__(self):
        return self.name

   