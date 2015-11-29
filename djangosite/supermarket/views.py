from django.shortcuts import render,render_to_response
from forms import LoginForm
from models import Employee
from django.contrib.auth import authenticate, login


# def login(request):
#     return render_to_response('login.html',{'mytitle':'login'})


def login(request):
    if request.method == "GET":
        return render_to_response("login.html", {'mytitle': 'login'})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # notice here
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active():
                    login(request, user)
                else:
                    # TODO
                    pass

            # if user:
            #     request.session["username"] = username
            # else:
            #     err = "incorrect username or password."
            #     return render_to_response("login.html", {"err": err})




