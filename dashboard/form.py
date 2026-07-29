from django import forms


from .models import Customer
from .models import cusignup
from .models import mddetail
from .models import addSupplier

class new_customer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'password']
    
    

class customer_signup(forms.ModelForm):
    class Meta:
        model=cusignup
        fields="__all__"

class md_detail(forms.ModelForm):
    class Meta:
        model=mddetail
        fields="__all__"

class supplierform(forms.ModelForm):
    class Meta:
        model=addSupplier
        fields="__all__"

    
    #supplier name

    def clean_suppliername(self):
        suppliername = self.cleaned_data['suppliername']

        if len(suppliername) < 3:
            raise forms.ValidationError(
                "Supplier name must be at least 3 characters."
            )

        return suppliername

    #companyname

    def clean_companyname(self):
        companyname=self.cleaned_data['companyname']

        if len(companyname) <2:
            raise forms.ValidationError(
                "Company Name must be at least 2 characters."
            )
        return companyname

    #contactperson

    def clean_contactperson(self):
        contactperson=self.cleaned_data['contactperson']

        if len(contactperson)<3:
            raise forms.ValidationError(
                "Name must be at least 3 characters."
            )
        return contactperson

    #mobile 

    def clean_mobile(self):
        mobile=self.cleaned_data['mobile']

        if not mobile.isdigit():
            raise forms.ValidationError(
                "Mobile Number Must Cantain only digits"
            )

        if len(mobile) !=10:
            raise forms.ValidationError(
                "Mobile must cantian 10 Numbers"
            )
        return mobile 

   
    # gstno
    def clean_gstno(self):
        gstno=self.cleaned_data['gstno']

        if len(gstno) <20:
            raise forms.ValidationError(
                "GST  Number must be 20 characters."
            )
        return gstno

    #druglicence

    def clean_druglicence(self):
        druglicence=self.cleaned_data['druglicence']

        if len(druglicence) !=5:
            raise forms.ValidationError(
                "Enter a valid Drug Licence Number"
            )
        return druglicence

    