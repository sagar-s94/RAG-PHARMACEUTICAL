from django.shortcuts import render,redirect
from django.contrib import messages
from .models import add_stock
from .models import out_stock
from decimal import Decimal
from django.db.models import Sum

from django.db.models import Q


# Create your views here.

def stockin(request):
    if request.method == "POST":
         
       
        medicineid = request.POST.get("medicineid")
        invoice = request.POST.get("invoice")
        medicinename = request.POST.get("medicinename")
        batchno = request.POST.get("batchno")
        currentstock = int(request.POST.get("currentstock"))
        newstock = int(request.POST.get("newstock"))
        unit = request.POST.get("unit")
        unitprice = Decimal(request.POST.get("unitprice"))
        totalamount =Decimal(max_digits=12, decimal_places=2)
        
        purchasedate = request.POST.get("purchasedate")
        supplier = request.POST.get("supplier")
        expiredate = request.POST.get("expiredate")
        status = request.POST.get("status")
        lastupdate = request.POST.get("lastupdate")
        remark = request.POST.get("remark")

          # Calculate total a
        currentstock = currentstock + newstock
        totalamount = unitprice * newstock

        add_stock.objects.create(
           
            medicineid=medicineid,
            invoice=invoice,
            medicinename=medicinename,
            batchno=batchno,
            currentstock=currentstock,
            newstock=newstock,
            unit=unit,
            unitprice=unitprice,
            totalamount=totalamount,
            
            purchasedate=purchasedate,
            supplier=supplier,
            expiredate=expiredate,
            status=status,
            lastupdate=lastupdate,
            remark=remark,
        )
    messages.success(request, "Stock added successfully!")
    return render(request,"stockreport/stockin.html")


def stockqty(request):
    qty=add_stock.objects.all()
    totalamount = qty.aggregate(
        total=Sum("totalamount")
    )["total"] or 0
  
    return render(request,"stockreport/stockqty.html",{"qty":qty ,"totalamount": totalamount})

def update_stock(request):
    detail= add_stock.objects.all()
    search=request.GET.get('search')
    if search:
        detail=add_stock.objects.filter(Q(medicineid__icontains=search) |
                                        Q(invoice__icontains=search) |
                                        Q(medicinename__icontains=search) |
                                        Q(batchno__icontains=search) |
                                        Q(purchasedate__icontains=search) |
                                        Q(supplier__icontains=search) |
                                        Q(remark__icontains=search))
        if detail.exists():
            messages.success(request, "Record found successfully.")
        else:
            messages.error(request, "Record not found.")

    return render(request,"stockreport/stock_update.html",{"detail":detail})

def stock_edit(request,id):
    edit=add_stock.objects.get(id=id)
    if request.method == "POST":
           edit.medicineid = request.POST.get("medicineid")
           edit.invoice = request.POST.get("invoice")
           edit.medicinename = request.POST.get("medicinename")
           edit.batchno = request.POST.get("batchno")
           edit.currentstock = request.POST.get("currentstock")
           edit.unit = request.POST.get("unit")
           edit.unitprice = request.POST.get("unitprice")
           edit.newstock = request.POST.get("newstock")
           edit.purchasedate = request.POST.get("purchasedate")
           edit.supplier = request.POST.get("supplier")
           edit.expiredate = request.POST.get("expiredate")
           edit.status = request.POST.get("status")
           edit.lastupdate = request.POST.get("lastupdate")
           edit.remark = request.POST.get("remark")
           edit.save()
           return redirect ('update_stock')


    return render(request,"stockreport/stock_edit.html",{"edit":edit})


def delect_stock(request,id):
    stock=add_stock.objects.get(id=id)
    stock.delete()
    return redirect('update_stock')







def stockout(request):
    if request.method =="POST":
        medicineid=request.POST.get('medicineid')
        invoice=request.POST.get('invoice')
        medicinename=request.POST.get('medicinename')
        batchno=request.POST.get('batchno')
        currentstock=int(request.POST.get('currentstock'))
        unit=request.POST.get('unit')
        unitprice=Decimal(request.POST.get('unitprice'))
        outstock=int(request.POST.get('outstock'))
        date=request.POST.get('date')
        customername=request.POST.get('customername')
        expiredate=request.POST.get('expiredate')
        status=request.POST.get('status')
        lastdate=request.POST.get('lastdate')
        remark=request.POST.get('remark')

        currentstock = currentstock - outstock
        totalamount = unitprice * outstock

        out_stock.objects.create(
            medicineid=medicineid,
            invoice=invoice,
            medicinename=medicinename,
            batchno=batchno,
            currentstock=currentstock,
            unit=unit,
            unitprice=unitprice,
            outstock=outstock,
            totalamount=totalamount,
            date=date,
            customername=customername,
            expiredate=expiredate,
            status=status,
            lastdate=lastdate,
            remark=remark
        )

  


    return render(request,"stockreport/stockout.html")

def stockout_qty(request):
    data=out_stock.objects.all()
    total_amount = out_stock.objects.aggregate(total=Sum("totalamount"))['total']

    

    return render(request,"stockreport/Stockout_qty.html",{"data":data,"total_amount":total_amount})

def stockout_update(request):
    result=out_stock.objects.all()
    search=request.GET.get('search')
    if search:
            result=out_stock.objects.filter(Q(medicineid__icontains=search) |
                                                Q(invoice__icontains=search) |
                                                Q(medicinename__icontains=search) |
                                                Q(batchno__icontains=search) |
                                               
                                                Q(customername__icontains=search) |
                                                Q(remark__icontains=search))
            print("Found:", result.count())
            if result.exists():
                    messages.success(request, "Record found successfully.")
            else:
                    messages.error(request, "Record not found.")
                    print("Found:", result.count())

    return render(request,"stockreport/stockout_update.html",{"result":result})



def stockout_edit(request,id):
    edit=out_stock.objects.get(id=id)
    if request.method == "POST":
        edit.medicineid=request.POST.get('medicineid')
        edit.invoice=request.POST.get('invoice')
        edit.medicinename=request.POST.get('medicinename')
        
        edit.batchno=request.POST.get('batchno')
        edit.currentstock=request.POST.get('currentstock')
        
        edit.unit=request.POST.get('unit')
        edit.unitprice=request.POST.get('unitprice')
        edit.outstock=request.POST.get('outstock')
        edit.date=request.POST.get('date')
        edit.customername=request.POST.get('customername')
        edit.expiredate=request.POST.get('expiredate')
        edit.status=request.POST.get('status')
        edit.lastdate=request.POST.get('lastdate')
        edit.remark=request.POST.get('remark')
        edit.save()
        return redirect ('stockoutupdate')



    return render(request,"stockreport/stockout_edit.html",{"edit":edit})

def stockout_delete(request,id):
    stock=out_stock.objects.get(id=id)
    stock.delete()
    return redirect('stockoutupdate')

     