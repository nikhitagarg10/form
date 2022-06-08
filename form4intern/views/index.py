from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from form4intern.models.userdata import Userdata
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.template import Context

class Index(View):
    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        Username = request.POST.get("Username")
        email = request.POST.get("email")
        adress = request.POST.get("adress")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pin")
        password1 = request.POST.get("pass1")
        password2 = request.POST.get("pass2")
        typee = request.POST.get("typee")
        #profile = request.POST.get("profile")
        try:
            profile = request.FILES["profile"]
            fs = FileSystemStorage()
            filename = fs.save(profile.name, profile)
            uploaded_file_url = fs.url(filename)
        except MultiValueDictKeyError:
            profile = False
        
        data = {
            "fname": fname,
            "lname": lname,
            "Username": Username,
            "email": email,
            "adress": adress,
            "city": city,
            "state": state,
            "pincode": pincode,
        }

        err = self.Validate(fname, lname, Username, email, adress, city, state, pincode, password1, password2, typee, profile)

        if (err == None):
            userdata = Userdata(    fname=fname, 
                                    lname=lname, 
                                    Username=Username, 
                                    email=email, 
                                    password=password1, 
                                    adress=adress, 
                                    city=city, 
                                    state=state, 
                                    pincode=pincode, 
                                    typee=typee,
                                    image=uploaded_file_url)
            userdata.password = make_password(userdata.password)
            userdata.register()

            return redirect("login")
        else:
            return render(request, "index.html",  {"data": data, "err": err})

    def get(self, request):
        go = request.GET.get("go")
        if (go == "login"):
            return redirect("login")
        return render(request, "index.html")
    
    def Validate(self, fname, lname, Username, email, adress, city, state, pincode, password1, password2, typee, profile):
        error = None 

        if (not fname):
            error = "first name required"
        elif (not lname):
            error = "last name required"
        elif (not Username):
            error = "Username is required"
        elif (not email):
                error = "email is required"
        elif (not typee):
                error = "please check the type of account"
        elif (not adress):
                error = "adress is required"
        elif (not city):
                error = "city is required"
        elif (not state):
                error = "state is required"
        elif (not pincode):
                error = "pincode is required"
        elif (len(pincode) != 6):
            error = "pincode needs have just 6 digits from 0 to 9"
        elif(not password1):
            error = "password is must"
        elif(password1 != password2):
            error = "passwords do not match"
        elif (len(password1) < 7):
            error = "password needs to be of 7 characters or more"

        p = Userdata.objects.filter(Username=Username)
        e = Userdata.objects.filter(email=email)

        if (p):
            error = "An account already exists with this Username"
        elif (e):
            error = "An account already exists with this email"

        return error
