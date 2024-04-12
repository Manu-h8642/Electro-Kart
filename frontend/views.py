from django.shortcuts import render,redirect
from backend.models import cdb,pdb
from frontend.models import contactdb,userdb,cartdb,billdb
from django.contrib import messages
# Create your views here.
def homepage(request):
    cat = cdb.objects.all()
    data = cartdb.objects.filter(uname=request.session['email'])
    x=0
    for i in data:
        x = x+i.qty
    return render(request,"home.html",{'cat':cat,'x':x})
def fproduct(request):
    pro = pdb.objects.all()
    data = cartdb.objects.filter(uname=request.session['email'])
    x = 0
    for i in data:
        x = x + i.qty
    return render(request,"fpro.html",{'pro':pro,'x':x})

def filtp(request,catname):
    data = pdb.objects.filter(cname=catname)
    dataa = cartdb.objects.filter(uname=request.session['email'])
    x = 0
    for i in dataa:
        x = x + i.qty
    return render(request,"filp.html",{'data':data,'x':x})

def viewp(request,pid):
    data = pdb.objects.filter(id=pid)
    dataa = cartdb.objects.filter(uname=request.session['email'])
    x = 0
    for i in dataa:
        x = x + i.qty
    return render(request,"vpro.html",{'data':data,'x':x})

def contact(request):
    dataa = cartdb.objects.filter(uname=request.session['email'])
    x = 0
    for i in dataa:
        x = x + i.qty
    return render(request,"cont.html",{'x':x})

def csave(request):
    if request.method == "POST":
        nn = request.POST.get('n')
        ee = request.POST.get('e')
        ss = request.POST.get('s')
        me = request.POST.get('m')
    obj = contactdb(name=nn,email=ee,sub=ss,msg=me)
    obj.save()
    messages.success(request, "Submitted Sucessfully.!")
    return redirect(contact)

def about(request):
    dataa = cartdb.objects.filter(uname=request.session['email'])
    x = 0
    for i in dataa:
        x = x + i.qty
    return render(request,"about.html",{'x':x})

def ser(request):
    dataa = cartdb.objects.filter(uname=request.session['email'])
    x = 0
    for i in dataa:
        x = x + i.qty
    return render(request,"service.html",{'x':x})

def userr(request):
    return render(request,"userl.html")

def usave(request):
    if request.method == "POST":
        nn = request.POST.get('n')
        ee = request.POST.get('e')
        pp = request.POST.get('pa')
        ii = request.FILES['im']
    obj = userdb(name=nn,email=ee,password=pp,img=ii)
    obj.save()
    messages.success(request, "Registered Sucessfully.!")
    return redirect(userr)

def ulogin(request):
    if request.method == "POST":
        ee = request.POST.get('e')
        pwd = request.POST.get('pas')
        if userdb.objects.filter(email=ee,password=pwd).exists():
            request.session['email']= ee
            request.session['password']= pwd
            messages.success(request, "Login Sucessfully.!")
            return redirect(homepage)
        else:
            messages.warning(request, "Something Wrong.!")
            return redirect(userr)
    messages.warning(request, "Something Wrong.!")
    return redirect(userr)

def ulogout(request):
    del request.session['email']
    del request.session['password']
    messages.warning(request, "Logout Sucessfully.!")
    return redirect(userr)

def savecart(request):
    if request.method == "POST":
        aa = request.POST.get('q')
        bb = request.POST.get('p')
        cc = request.POST.get('un')
        dd = request.POST.get('pn')
        ee = request.POST.get('tp')
    obj = cartdb(uname=cc,pname=dd,qty=aa,price=bb,tprice=ee)
    obj.save()
    messages.success(request, "Product Added Successfully.!")
    return redirect(fproduct)

def cartpage(request):
    data = cartdb.objects.filter(uname=request.session['email'])
    tprice = 0
    for i in data:
        tprice = tprice+i.tprice
    return render(request,"cartpage.html",{'data':data, 'tprice':tprice})

def deletecart(request,did):
    x = cartdb.objects.filter(id=did)
    x.delete()
    messages.success(request, "Removed Successfully.!")
    return redirect(cartpage)

def checkout(request):
    data = cartdb.objects.filter(uname=request.session['email'])
    e = userdb.objects.get(email=request.session['email']).name
    tprice = 0
    for i in data:
        tprice = tprice+i.tprice
    return render(request,"chekout.html",{'data':data,'tprice':tprice,'e':e})

def savecheck(request):
    if request.method == "POST":
        aa = request.POST.get('un')
        bb = request.POST.get('em')
        cc = request.POST.get('ad')
        dd = request.POST.get('ci')
        ee = request.POST.get('co')
        ff = request.POST.get('code')
        gg = request.POST.get('tel')
        obj = billdb(uname=aa, email=bb, address=cc,city=dd,country=ee,code=ff,phone=gg)
        obj.save()
        messages.success(request, "Successfully Saved.!")
        return redirect(checkout)