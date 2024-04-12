from django.shortcuts import render,redirect
from backend.models import cdb,pdb
from frontend.models import contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def category(request):
    return render(request,"category.html")

def save(request):
    if request.method == "POST":
        aa = request.POST.get('n')
        bb = request.POST.get('d')
        cc = request.FILES['img']
        obj = cdb(name=aa,des=bb,image=cc)
        obj.save()
        messages.success(request,"Category Sucessfully Saved.!")
        return redirect(category)

def disp(request):
    data = cdb.objects.all()
    return render(request,"table.html",{'data':data})

def edit(request,cid):
    data = cdb.objects.get(id=cid)
    return render(request,"edit.html",{'data':data})

def update(request,cid):
    if request.method == "POST":
        aa = request.POST.get('n')
        bb = request.POST.get('d')
        try:
            img = request.FILES["img"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = cdb.objects.get(id=cid).image
        cdb.objects.filter(id=cid).update(name=aa,des=bb,image=file)
        messages.success(request, "Category Updated Sucessfully.!")
        return redirect(disp)

def delete(request,cid):
    x = (cdb.objects.filter(id=cid))
    x.delete()
    messages.success(request, "Category Deleted Sucessfully.!")
    return redirect(disp)

def prod(request):
    cat = cdb.objects.all()
    return render(request,"product.html",{'cat':cat})

def psave(request):
    if request.method == "POST":
        aa = request.POST.get('cn')
        bb = request.POST.get('n')
        cc = request.POST.get('d')
        gg = request.POST.get('p')
        dd = request.FILES['img']
        ee = request.FILES['img1']
        ff = request.FILES['img2']
        obj = pdb(cname=aa,pname=bb,desc=cc,price=gg,image1=dd,image2=ee,image3=ff)
        obj.save()
        messages.success(request, "Category Sucessfully Saved.!")
        return redirect(prod)

def pdisp(request):
    data = pdb.objects.all()
    return render(request,"ptable.html",{'data':data})

def pedit(request,pid):
    cat = cdb.objects.all()
    data = pdb.objects.get(id=pid)
    return render(request,"pedit.html",{'data':data,'cat':cat})

def pupdate(request,pid):
    if request.method == "POST":
        aa = request.POST.get('cn')
        bb = request.POST.get('n')
        cc = request.POST.get('d')
        gg = request.POST.get('p')
        try:
            img = request.FILES["img"]
            fs = FileSystemStorage()
            file1 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file1 = pdb.objects.get(id=pid).image1
        try:
            img1 = request.FILES["img1"]
            fs = FileSystemStorage()
            file2 = fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file2 = pdb.objects.get(id=pid).image2
        try:
            img2 = request.FILES["img2"]
            fs = FileSystemStorage()
            file3 = fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file3 = pdb.objects.get(id=pid).image3
        pdb.objects.filter(id=pid).update(cname=aa,pname=bb,desc=cc,price=gg,image1=file1,image2=file2,image3=file3)
        messages.success(request, "Category Updated Sucessfully.!")
        return redirect(pdisp)

def pdelete(request,pid):
    x = (pdb.objects.filter(id=pid))
    x.delete()
    messages.success(request, "Category Deleted Successfully.!")
    return redirect(pdisp)
def adlog(request):
    return render(request,"adminl.html")

def alog(request):
    if request.method == "POST":
        un = request.POST.get('un')
        pw = request.POST.get('pa')
        if User.objects.filter(username__contains=un).exists():
            xx = authenticate(username=un,password=pw)
            if xx is not None:
                login(request,xx)
                request.session['username']=un
                request.session['password']=pw
                messages.success(request, "Login Successfully.!")
                return redirect(index)
            else:
                messages.error(request, "Check Password.!")
                return redirect(adlog)
        else:
            messages.warning(request, "Check username.!")
            return redirect(adlog)

def adlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully.!")
    return redirect(adlog)

def contview(request):
    data = contactdb.objects.all()
    return render(request,"contactv.html",{'data':data})

def cdel(request,cid):
    x=(contactdb.objects.filter(id=cid))
    x.delete()
    messages.success(request, "Deleted Successfully.!")
    return redirect(contview)
