from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from form4intern.models.userdata import Userdata

class Login(View):
    def post(self, request):
        Username = request.POST.get("Username")
        email = request.POST.get("email")
        typee = request.POST.get("typee")
        password = request.POST.get("pass")
        
        data = {
            "Username": Username,
            "email": email,
        }

        err = self.Validate(Username, email, password, typee)

        if (err == False):
            u = Userdata.objects.get(Username = Username)
            return render(request, "dashboard.html", {"u": u})
        else:
            return render(request, "login.html",  {"data": data, "err": err})


    def get(self, request):
        go = request.GET.get("go")
        if (go == "signup"):
            return redirect("index")
        return render(request, "login.html")
    
    def Validate(self, Username, email, password, typee):
        err = False

        if (not Username):
            err = "please enter your username"
        elif(not email):
            err = "please enter your e-mail"
        elif(not typee):
            err = "please Check in with the type of account"
        elif (not password):
            err = "passowrd is must"

        if (err == False):
            u_obj = Userdata.objects.filter(Username = Username)
            if (u_obj):
                for u in u_obj:
                    ans = check_password(password, u.password)
                    if (u.email != email):
                        err = "E-Mail entered in incorrect"
                    elif (u.typee != typee):
                        err = f" There is no {typee} account with {Username} registered with us"
                    elif (ans==False):
                        err = "entered password is incorrect"
                    elif (ans == True):
                        err = False
            else:
                err = f"Username is incorrect"
        return err