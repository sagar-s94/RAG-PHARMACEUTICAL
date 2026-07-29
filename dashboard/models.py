from django.db import models



# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed=True
        db_table= "signup"


class cusignup(models.Model):
    PROFESSION_CHOICES = [
    ("Customer", "Customer"),
    ("Doctor", "Doctor"),
    ("Pharmacist", "Pharmacist"),
    ("Nurse", "Nurse"),
    ("Hospital Staff", "Hospital Staff"),
    ("Clinic Staff", "Clinic Staff"),
    ("Medical Representative", "Medical Representative"),
    ("Other", "Other"),
]
    
    ORGANIZATION_CHOICES = [
    ("Hospital", "Hospital"),
    ("Clinic", "Clinic"),
    ("Pharmacy", "Pharmacy"),
    ("Medical Store", "Medical Store"),
    ("Nursing Home", "Nursing Home"),
    ("Diagnostic Laboratory", "Diagnostic Laboratory"),
    ("Medical College", "Medical College"),
    ("Healthcare Company", "Healthcare Company"),
    ("Pharmaceutical Company", "Pharmaceutical Company"),
    ("Distributor", "Distributor"),
    ("Wholesaler", "Wholesaler"),
    ("NGO / Health Organization", "NGO / Health Organization"),
    ("Other", "Other"),
]


    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,unique=True)
    profession=models.CharField(max_length=50,choices=PROFESSION_CHOICES,default="profession")
    organization=models.CharField(max_length=50,choices=ORGANIZATION_CHOICES,default="organization")
    city=models.CharField(max_length=100,default="city")
    password=models.CharField(max_length=255)


    def __str__(self):
        return self.name
    
class contact_us(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class mddetail(models.Model):
    pre=[
       ( 'Yes','Yes'),
       ('No','No'),
    ]

    form= [
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
        
    avil=[
        ('In Stock','In Stock'),
        ('Out of Stock','Out of Stock')
    ]

    id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='medicine_images/',max_length=500)
    mdname=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    form=models.CharField(max_length=50,choices=form)
    packingsize=models.CharField(max_length=50)
    price=models.CharField(max_length=100)
    availability=models.CharField(max_length=50,choices=avil)
    description=models.TextField()
    used=models.TextField()
    sideeffect=models.TextField()
    prescription=models.CharField(max_length=20,choices=pre)
    expirydate=models.DateField()

    def __str__(self):
        return self.name



class addSupplier(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    supplierid = models.AutoField(primary_key=True)
    suppliername = models.CharField(max_length=30)
    companyname = models.CharField(max_length=50)
    contactperson = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    gstno = models.CharField(max_length=15,null=True,blank=True)
    druglicence = models.CharField(max_length=30,null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def __str__(self):
        return self.suppliername

    

 