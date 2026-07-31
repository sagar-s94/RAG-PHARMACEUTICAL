from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from .models import Customer
from .models import cusignup
from .models import  contact_us
from .models import mddetail
from .models import addSupplier
from inventory.models import out_stock
from .form import new_customer
from .form import customer_signup
from django.contrib.auth.hashers import check_password, make_password
from medicine.models import allopathy_medicine
from medicine.models import ayurvedic_medicine
from django.db.models import Q
# Create your views here.

# def customer(request):
#      return render(request, "index.html")
 
        
def dashboard(request):
   if "user_id" not in request.session:
    return redirect("'login.html") 
   detail=contact_us.objects.all()
   return render(request, "index.html",{"data":detail})

def register(request):
    if request.method == "POST":
        form = new_customer(request.POST)
        if form.is_valid():
            form.save()  # ModelForm can save directly!
        return redirect("dashboard")
    else:
        form = new_customer()

    return render(request, 'register.html', {'form': form})


def cu_signup(request):
    if request.method == "POST":
        form = customer_signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect("customerhome")
        else:
            print(form.errors)
    else:
        
        form = customer_signup()

    return render(request,"cu_signup.html",{'form':form}) 



    

def login(request):

    if request.method == "POST":

        phone = request.POST.get("phone")
        password = request.POST.get("password")

        user = Customer.objects.filter(phone=phone).first()
        print("User found:", user)

        if user:
            if check_password(password, user.password):

                request.session["user_id"] = user.id
                request.session["user_name"] = user.name

                return redirect("dashboard")

            else:
                return render(request, "login.html",
                              {"message": "Incorrect Password"})

        else:
            return render(request, "login.html",
                {"message": "Phoneno does not exist"})
    return render (request,"login.html")

def admin_logout(request):
    request.session.flush()   # Remove all session data
    return redirect("login")

        


def cust_login(request):
    if request.method == "POST":
        phone= request.POST.get("phone")
        password = request.POST.get("password")

        user= cusignup.objects.filter(phone=phone).first()
        if user:
            if check_password(password, user.password):
                request.session["user_id"]=user.id
                request.session["user_name"]=user.name

                return redirect("customerhome")
            else:
                return render(request,"cust_login.html",{"message":"Password does not match"})
        else:
            return render (request,"cust_login.html")
        
        
    return render(request,"cust_login.html",
        {"message": "Invalid phone number or password"
        })

def cust_logout(request):
    request.session.flush()   # Remove all session data
    return redirect("cust_login")




def cust_profile(request):
    custmore_profile=request.session.get("user_id")

    if not custmore_profile:
        return redirect("cust_login")
    
    profile=cusignup.objects.get(id=custmore_profile)
    return render(request,"cust_profile.html",{"profile":profile})







def customer_home(request):
    if "user_id" not in request.session:
        return redirect("cust_login") 
    test = allopathy_medicine.objects.all()
    detail=ayurvedic_medicine.objects.all()
   
    return render(request,"cust_home.html",{"data":test,"data":detail})

def cust_contactus(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            address = request.POST.get("address")

            contact_us.objects.create(
                name=name,
                phone=phone,
                address=address,
            )

            messages.success(request, "Your details have been submitted successfully.")
            return redirect("customerhome")   # Redirect to same page

        except Exception as e:
            print("Error:", e)  # Print the actual error in the terminal
            messages.error(request, f"Failed to submit the form: {e}")
            return redirect("customerhome")

    return render(request, "customerhome")

    # return render(request,"cust_home.html")



def medicine_detail(request):
    if request.method == "POST":
        
        image=request.FILES.get('image')
        mdname=request.POST.get('mdname')
        brand=request.POST.get('brand')
        category=request.POST.get('category')
        form=request.POST.get('form')
        packingsize=request.POST.get('packingsize')
        price=request.POST.get('price')
        availability=request.POST.get('availability')
        description=request.POST.get('description')
        used=request.POST.get('used')
        sideeffect=request.POST.get('sideeffect')
        prescription=request.POST.get('prescription')
        expirydate=request.POST.get('expirydate')
    try:    
        mddetail.objects.create(
            
            image=image,
            mdname=mdname,
            brand=brand,
            category=category,
            form=form,
            packingsize=packingsize,
            price=price,
            availability=availability,
            description=description,
            used=used,
            sideeffect=sideeffect,
            prescription=prescription,
            expirydate=expirydate
        )
        messages.success(request, "Medicine added successfully.")
        return render(request,"med_detail.html")
    
    except Exception:
        messages.error(request, "Failed to add medicine. Please try again.")
        return render(request,"med_detail.html")

def detail_card(request):
    detail=mddetail.objects.all()

    return render(request,'cust_mddetail.html',{"data":detail})


def update_detail(request):
    md=mddetail.objects.all()
    search=request.GET.get('search')
    
    if search:
        md=mddetail.objects.filter(mdname__icontains=search)
        if md.exists():
            messages.success(request, "Record found successfully.")
        else:
            messages.error(request, "Record not found.")

        
    
    return render(request,"med_deupdate.html",{"md":md})

def edit_detail(request,id):
    detail=mddetail.objects.get(id=id)

    if request.method == "POST":
        detail.image=request.FILES.get('image')
        detail.mdname=request.POST.get('mdname')
        detail.brand=request.POST.get('brand')
        detail.category=request.POST.get('category')
        detail.form=request.POST.get('form')
        detail.packingsize=request.POST.get('packingsize')
        detail.price=request.POST.get('price')
        detail.availability=request.POST.get('availability')
        detail.description=request.POST.get('description')
        detail.used=request.POST.get('used')
        detail.sideeffect=request.POST.get('sideeffect')
        detail.prescription=request.POST.get('prescription')
        detail.expirydate=request.POST.get('expirydate')

        detail.save()
        return redirect('updatedetial')
    
    return render(request,"med_edit.html",{"detail":detail})

def delete_detail(request,id):
    detail= get_object_or_404(mddetail,id=id)
    detail.delete()
    return redirect ('detailcard')

def admin_mddetail_card(request):
    detail=mddetail.objects.all()
    return render(request,"admin.mddetal.html",{"data":detail})

 


def addsupplier(request):
    if request.method == "POST":
       
        suppliername=request.POST.get('suppliername')
        companyname=request.POST.get('companyname')
        contactperson=request.POST.get('contactperson')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        gstno=request.POST.get('gstno')
        druglicence=request.POST.get('druglicence')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        status=request.POST.get('status')

        addSupplier.objects.create(
            
            suppliername=suppliername,
            companyname=companyname,
            contactperson=contactperson,
            mobile=mobile,
            email=email,
            gstno=gstno,
            druglicence=druglicence,
            address=address,
            city=city,
            state=state,
            status=status,

        )


    return render(request,"supplier/addsupplier.html")
        
def suppliar_list(request):
    list=addSupplier.objects.all()
     
    return render(request,"supplier/suppliar_list.html",{"list":list})


def suppliar_update(request):
    data=addSupplier.objects.all()
    search=request.GET.get('search')

    if search:
        data=addSupplier.objects.filter(Q(supplierid__icontains=search) |
            Q(suppliername__icontains=search) |
            Q(companyname__icontains=search) |
            Q(contactperson__icontains=search) |
            Q(mobile__icontains=search) |
            Q(email__icontains=search) |
            Q(gstno__icontains=search) |
            Q(druglicence__icontains=search) |
            Q(address__icontains=search) |
            Q(city__icontains=search) |
            Q(state__icontains=search) |
            Q(status__icontains=search)
            )
        if data.exists():
            messages.success(request, "Record found successfully.")
        else:
            messages.error(request, "Record not found.")

    return render(request,"supplier/suppliar_update.html",{"data":data})

def suppliar_edit(request,supplierid):
    edit=addSupplier.objects.get(supplierid=supplierid)
    if request.method == "POST":
        edit.supplierid=request.POST.get('supplierid')
        edit.suppliername=request.POST.get('suppliername')
        edit.companyname=request.POST.get('companyname')
        edit.contactperson=request.POST.get('contactperson')
        edit.mobile=request.POST.get('mobile')
        edit.email=request.POST.get('email')
        edit.gstno=request.POST.get('gstno')
        edit.druglicence=request.POST.get('druglicence')
        edit.address=request.POST.get('address')
        edit.city=request.POST.get('city')
        edit.state=request.POST.get('state')
        edit.status=request.POST.get('status')

        edit.save()
        return redirect("suppliarupdate")

    return render(request,"supplier/suppliaredit.html",{"edit":edit})


def supplier_delete(request, supplierid):
    supplier = addSupplier.objects.get(supplierid=supplierid)
    supplier.delete()
    return redirect("supplier/supplier_update")

def invoice(request,):
    data=out_stock.objects.all()
    total_amount = out_stock.objects.aggregate(total=Sum("totalamount"))['total']

    
    search=request.GET.get('search')
    if search:
        data=out_stock.objects.filter(Q(medicineid__icontains=search) |
                                        Q(invoice__icontains=search) |
                                        Q(medicinename__icontains=search) |
                                        Q(batchno__icontains=search) |
                                                   
                                        Q(customername__icontains=search) |
                                        Q(remark__icontains=search))
       
        if data.exists():
            messages.success(request, "Record found successfully.")
        else:
            messages.error(request, "Record not found.")
            
    
    
    return render(request,"invoice.html",{"data":data,"total_amount":total_amount})

def gen_invoice(request,id):
    invoice=out_stock.objects.get(id=id)

    total_amount = invoice.totalamount

    context = {
        "sale": invoice,
        "total_amount": total_amount,
    }


    return render(request,"geninvoice.html",context)
