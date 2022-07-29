from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *



########################  INDEX  ########################################

def index(request):
    if 'user' in request.session:
        current_user=request.session['user']
        param={'current_user':current_user}
        return render(request,'uindex.html',param)

    elif 'admin' in request.session:
        current_admin=request.session['admin']
        param={'current_admin':current_admin}
        return render(request,'aindex.html',param)

    else:
        return render(request,'index.html')

def about(request):
    return render(request,"abt1.html")
def products(request):
    data=add_pro.objects.all()
    return render(request,"services.html",{"data":data})


#############################  LOGIN  ##############################

def login(request):
    if request.method=="POST":
        email=request.POST.get('umail')
        psw=request.POST.get('upsw')
        check_user = usmodel.objects.filter(umail=email,upsw=psw)
        if check_user:
            request.session['user']=email
            return redirect('uindex')
        elif email=="admin@gmail.com" and psw=="admin":
            request.session['admin']=email
            return redirect('aindex')
        else:
            return HttpResponse('enter valid email or password')
    return render(request,'login.html')

def user_signup(request):
    if request.method =='POST':
        uname=request.POST.get('uname')
        uage=request.POST.get('uage')
        uphone=request.POST.get('uphone')
        umail= request.POST.get('umail')
        upsw = request.POST.get('upsw')
        if usmodel.objects.filter(umail=umail).count()>0:
            return HttpResponse('email already exists.')
        else:
            user = usmodel(umail=umail,upsw=upsw,uname=uname,uage=uage,uphone=uphone)
            user.save()
            return redirect('login')
    else:
        return render(request,'usignup.html')

###################  LOGOUT  #####################


def user_logout(request):
    try:
        del request.session['user']
    except:
        return redirect('index')
    return redirect('index')

def admin_logout(request):
    try:
        del request.session['admin']
    except:
        return redirect('index')
    return redirect('index')


###################  ADMIN_FUNCTIONS  #############

#1
def add_products(request):
    if request.method=="POST":
        a = add_proforms(request.POST, request.FILES)
        if a.is_valid():
            pcompany = a.cleaned_data['pcompany']
            pname = a.cleaned_data['pname']
            file = a.cleaned_data['file']
            pram = a.cleaned_data['pram']
            prom = a.cleaned_data['prom']
            pcolor = a.cleaned_data['pcolor']
            pprice = a.cleaned_data['pprice']
            pitems = a.cleaned_data['pitems']
            b = add_pro(pcompany=pcompany,pname=pname,file=file,pram=pram,prom=prom,pcolor=pcolor,pprice=pprice,pitems=pitems)
            b.save()
            return redirect("aindex")
        else:
            return HttpResponse("failed")
    return render(request, "addproducts.html")

#2
def view_admin_products(request):
    products = add_pro.objects.all()
    return render(request, "viewproducts.html", {"data": products})

#3
def update_product(request):
    products=add_pro.objects.all()
    return render(request,"update_product.html",{"data":products})

def update(request,id):
    a=add_pro.objects.filter(id=id)
    return render(request,"update.html",{"data":a})

def update1(request):
    if request.method=="POST":
        # file = request.POST.get('file')
        pcompany=request.POST.get('pcompany')
        pname = request.POST.get('pname')
        pram = request.POST.get('pram')
        prom=request.POST.get('prom')
        pcolor=request.POST.get('pcolor')
        pprice=request.POST.get('pprice')
        pitems=request.POST.get('pitems')
        ID=request.POST.get('id')
        add_pro.objects.filter(id=ID).update(pcompany=pcompany,pname=pname,pram=pram,prom=prom,pcolor=pcolor,pprice=pprice,pitems=pitems)
        return redirect('updateproducts')
    else:
        return HttpResponse("failed")


#4
def delete_pro(request):
    products = add_pro.objects.all()
    return render(request, "delete_product.html", {"data": products})

def del1(request,pname):
    try:
        record = add_pro.objects.get(pname=pname)
        record.delete()
        return redirect("delete_products")
    except:
        return HttpResponse("Record doesn't exists")

#5
def bookings(request):
    data=Book.objects.all()
    return render(request,"bookings.html",{"data":data})

#6
def view_feedback(request):
    feedback=feedbackmodel.objects.all()
    return render(request,"view_feedback.html",{"feedback":feedback})
def detete_feedback(request,email):
    try:
        record = feedbackmodel.objects.get(email=email)
        record.delete()
        return redirect("feedback")
    except:
        return HttpResponse("Record doesn't exists")

def aindex(request):
    return render(request,"aindex.html")



########################  USER_FUNCTIONS  ##################


def user_index(request):
    return render(request,"uindex.html")
def uabout(request):
    return render(request,"uabout.html")
def ucontact(request):
    if request.method == "POST":
        name = request.POST.get('cname')
        email = request.POST.get('cmail')
        sub = request.POST.get('csub')
        mes = request.POST.get('cmes')
        dt = request.POST.get('dt')
        feedback = feedbackmodel(name=name, email=email, sub=sub, mes=mes, dt=dt)
        feedback.save()
        return redirect('ucontact')

    else:
        return render(request, 'ucontact.html')


#1
def view_user_pro(request):
    if 'user' in request.session:
        current_user=request.session['user']
        products=add_pro.objects.all()
        return render(request,"viewuser_products.html",{"data":products,"user":current_user})


#2
def placeorder(request,id):
        a = add_pro.objects.filter(id=id)
        if request.method == 'POST':
            prid = request.POST.get('pname')
            dmail = request.POST.get('dmail')
            qty = request.POST.get('qty')
            name = request.POST.get('dname')
            number = request.POST.get('dnum')
            address = request.POST.get('dadd')
            pincode = request.POST.get('dpin')
            dt = request.POST.get('dt')
            lmark = request.POST.get('lmark')
            dtype = request.POST.get('dtype')
            order = add_pro.objects.get(id=prid)
            if order:
                if order.pitems >= int(qty):
                    pname=order.pname
                    total=int(qty) * order.pprice
                    pcolor=order.pcolor
                    rem=order.pitems-int(qty)
                    file=order.file
                    pid=order.id
                    pprice=order.pprice
                    pram=order.pram
                    prom=order.pram
                    quantity=qty
                    add_pro.objects.filter(id=prid).update(pitems=rem)
                    book = Book.objects.create(pname=pname, pcolor=pcolor, total=total, file=file,
                                               pram=pram, prom=prom,pprice=pprice,dmail=dmail,quantity=quantity,
                                               name=name,number=number,address=address,pincode=pincode,
                                               dtype=dtype,dt=dt,lmark=lmark,pid=pid,
                                               status='BOOKED',payment='payal')
                    book.save()
                    return render(request,"paypal.html",{"a":book.id})
                else:
                    return HttpResponse("FAILED")
        if 'user' in request.session:
            current_user = request.session['user']
            # param={'current_user':current_user}
        # else:
            return render(request, 'placeorder.html',{"data":a,"current_user":current_user},)

def paypal_pay(request):
    return render(request,"paypal.html")
def pay(request):
    # Book.objects.filter(id=id).update(payment="Cash On Delevery")
    return redirect('uindex')



#3
def cancel(request,id):
    a=Book.objects.filter(id=id)
    return render(request,"cancel.html",{"data":a})
def cancellings(request):
    if request.method == 'POST':
        c_id = request.POST.get('cid')
        order = Book.objects.get(id=c_id)
        if order:
            pid=order.pid
            pro = add_pro.objects.get(id=pid)
            rem = pro.pitems + order.quantity
            add_pro.objects.filter(id=pid).update(pitems=rem)
            Book.objects.filter(id=c_id).update(status='CANCELLED')
            return redirect('uindex')
        else:
            return HttpResponse("failed")
    return render(request,"cancel.html")





#5
def view_book(request):
    # if request.method == 'POST':
    if 'user' in request.session:
        current_user=request.session['user']
        # param={'current_user':current_user}
        MAIL = current_user
        STATUS = 'BOOKED'
        data = Book.objects.filter(dmail=MAIL, status=STATUS)
        return render(request, "myorder.html", {"a": data})
    else:
        return HttpResponse("f")

def view_cancel(request):
    if 'user' in request.session:
        current_user = request.session['user']
        MAIL = current_user
        STATUS = 'CANCELLED'
        data = Book.objects.filter(dmail=MAIL, status=STATUS)
        return render(request, "myorder.html", {"a": data})
    else:
        return HttpResponse("f")

#6
def contact(request):
    if request.method=="POST":
        name= request.POST.get('cname')
        email= request.POST.get('cmail')
        sub= request.POST.get('csub')
        mes= request.POST.get('cmes')
        dt=request.POST.get('dt')
        feedback=feedbackmodel(name=name,email=email,sub=sub,mes=mes,dt=dt)
        feedback.save()
        return redirect('contact')

    else:
        return render(request, 'contact.html',)

########################  payment ########################




def cart1(request,id,user):
    a=add_pro.objects.get(id=id)
    us=user
    if a:
        # return HttpResponse("s")
        pname=a.pname
        pprice=a.pprice
        pram=a.pram
        prom=a.prom
        file=a.file
        pcolor=a.pcolor
        b=cart.objects.create(pname=pname,pprice=pprice,prom=prom,pram=pram,file=file,pcolor=pcolor,us=us)
        b.save()
        return redirect('cart')
    else:
        return HttpResponse("f")

    return render(request,"viewuser_products.html",{"data":a})
def cart2(request):
    if 'user' in request.session:
        current_user = request.session['user']
        data=cart.objects.filter(us=current_user)
        return render(request,"cart.html",{"data":data})
def del_cart(request,id):
    try:
        record = cart.objects.get(id=id)
        record.delete()
        return redirect("cart")
    except:
        return HttpResponse("Record doesn't exists")