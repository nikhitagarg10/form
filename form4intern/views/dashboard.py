from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from form4intern.models.userdata import Userdata

class Login(View):
    def post(self, request):
        pass
    def get(self, request):
        go = request.GET.get("go")
        if (go == "login"):
            return redirect("login")
        return render(request, "dashboard.html")