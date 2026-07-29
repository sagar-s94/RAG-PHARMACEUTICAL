from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import allopathy_medicine
from .models import ayurvedic_medicine
# Create your views here.


def medicine(request):
     return render(request,"medicine.html")

def total_medicine(request):
    test = allopathy_medicine.objects.all()
    detail=ayurvedic_medicine.objects.all()
   
    return render(request,"total_medicine.html",{"data":test,"result":detail})



#ayurvedic Category
def ayurvedic_medicine_add(request):
    
    
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        category=request.POST.get('category')
        company=request.POST.get('company')
        quantity=request.POST.get('quantity')
        packing_size=request.POST.get('packing_size')
        price=request.POST.get('price')
        expirydate=request.POST.get('expirydate')
        

        ayurvedic_medicine.objects.create(
            id=id,
            name=name,
            category=category,
            company=company,
            quantity=quantity,
            packing_size=packing_size,
            price=price,
            expirydate=expirydate,
           
        )
    
    added=ayurvedic_medicine.objects.all()

    return render(request,"ayurvedic/add.html",{"data":added})

def ayurvedic_medicine_delete(request,id):
    medicine = get_object_or_404(ayurvedic_medicine, id=id)
    medicine.delete()
    return redirect("ayurvedic_medicine_update") 


def ayurvedic_medicine_update(request):
    md=ayurvedic_medicine.objects.all()

    search=request.GET.get("search")

    if search:
        md=ayurvedic_medicine.objects.filter( name__icontains=search)

  

    return render(request,"ayurvedic/update.html", {"md":md})

def ayurvedic_medicine_veiwdetail(request):
    detail=ayurvedic_medicine.objects.all()
    return render(request,"ayurvedic/veiwdetail.html",{"data":detail})

#allopathy_medicine cetagory

def allopathy_medicine_add(request):
     
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        category=request.POST.get('category')
        company=request.POST.get('company')
        quantity=request.POST.get('quantity')
        packing_size=request.POST.get('packing_size')
      
        price=request.POST.get('price')
        expirydate=request.POST.get('expirydate')
       

        allopathy_medicine.objects.create(
            id=id,
            name=name,
            category=category,
            company=company,
            quantity=quantity,
            packing_size=packing_size,
            
            price=price,
            expirydate=expirydate,
           
 )
    add=allopathy_medicine.objects.all()
    return render(request,"allopathy/add.html",{"data":add})


def allopathy_medicine_delete(request,id):

  
    medicine = get_object_or_404(allopathy_medicine, id=id)
    medicine.delete()
    return redirect("allopathy_medicine_update") 

def allopathy_medicine_update(request):

    medicines = allopathy_medicine.objects.all()

    search = request.GET.get("search")

    if search:
        medicines = allopathy_medicine.objects.filter(
            name__icontains=search
        )

    return render(request, "allopathy/update.html", {
        "medicines": medicines
    })
       





def edit_medicine(request, id):

    medicine = allopathy_medicine.objects.get(id=id)

    if request.method == "POST":

        medicine.name = request.POST.get("name")
        medicine.category = request.POST.get("category")
        medicine.company = request.POST.get("company")
        medicine.quantity = request.POST.get("quantity")
        medicine.packing_size = request.POST.get("packing_size")
        medicine.price = request.POST.get("price")
        medicine.expirydate = request.POST.get("expirydate")

        medicine.save()

        return redirect("allopathy_medicine_update")

    return render(request, "allopathy/edit.html", {
        "medicine": medicine
    })

def edit_ayurvedic(request,id):
    md=ayurvedic_medicine.objects.get(id=id)

    if request.method == "POST":
        md.name=request.POST.get("name")
        md.category = request.POST.get("category")
        md.company = request.POST.get("company")
        md.quantity = request.POST.get("quantity")
        md.packing_size = request.POST.get("packing_size")
        md.price = request.POST.get("price")
        md.expirydate = request.POST.get("expirydate")

        md.save()

        return redirect("ayurvedic_medicine_update")
        
    return render(request,"ayurvedic/edit.html",{"data":md})




def allopathy_medicine_veiwdetail(request):
    test = allopathy_medicine.objects.all()
    return render(request,"allopathy/veiwdetail.html",{"data":test})