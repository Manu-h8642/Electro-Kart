from django.urls import path
from frontend import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('fproduct/',views.fproduct,name="fproduct"),
    path('filtp/<catname>/',views.filtp,name="filtp"),
    path('viewp/<int:pid>/',views.viewp,name="viewp"),
    path('contact/',views.contact,name="contact"),
    path('csave/',views.csave,name="csave"),
    path('about/',views.about,name="about"),
    path('ser/',views.ser,name="ser"),
    path('userr/',views.userr,name="userr"),
    path('usave/',views.usave,name="usave"),
    path('ulogin/',views.ulogin,name="ulogin"),
    path('ulogout/',views.ulogout,name="ulogout"),
    path('savecart/',views.savecart,name="savecart"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('deletecart/<int:did>/',views.deletecart,name="deletecart"),
    path('checkout/',views.checkout,name="checkout"),
    path('savecheck/',views.savecheck,name="savecheck"),
]