from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r"^purchase/", views.purchase, name="purchase"),
    #url(r"^supply/", views.supply, name="supply"),
    url(r"login/", views.login, name="login"),
]




