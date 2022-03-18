import imp
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        user = User.objects.filter(email=email).exists()

        if password1 != password2:
            messages.error(request, "Both Password are different")
            return redirect("/sign-up")
        
        elif user:
            messages.error(request, "User with this Username/email id already exists.")
            return redirect("/sign-up")

        else:
            new_user = User.objects.create_user(username=username, email=email, password=password1)
            new_user.save()

            username = User.objects.get(email=email)
            user = authenticate(username=username, password=password1)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Account created successfully")
                return redirect('/')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,"Username doesn\'t exist, Please Register")
            return render(request, 'login.html')

        else:
            auth.login(request, user)
            messages.success(request, "Loggedin Successfully")
            return redirect('/')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')
