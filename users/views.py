from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User
from pdf.models import Pdf


def kirish(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.save()
            return redirect('/')
        else:
            messages.warning(request, 'Id yoki parol xato')
            return redirect('/kirish')

    return render(request, 'kirish/login.html')


def home(request):
    userlar = User.objects.all
    contex = {
        'userlar': userlar,
    }
    return render(request, 'boshi/home.html', contex)

def royhat(request):
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']
        sharif = request.POST['sharif']
        t_yil = request.POST['t_yil']
        t_nomer = request.POST['t_nomer']
        k_yil = request.POST['k_yil']
        gender = request.POST['gender']
        talim_turi = request.POST['talim_turi']

        fakultet = request.POST['fakultet']
        yonalish = request.POST['yonalish']
        kurs = request.POST['kurs']
        guruh = request.POST['guruh']           

        viloyat = request.POST['viloyat']
        tuman = request.POST['tuman']
        mfy = request.POST['mfy']
        kocha_uy = request.POST['kocha_uy']
              
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday ID mavjud'        
        else:
            user = get_user_model().objects.create(lavozim='talaba', username = username, last_name = familya, first_name = ism, sharif=sharif, t_yil=t_yil, t_nomer=t_nomer, k_yil=k_yil, gender=gender, talim_turi=talim_turi, fakultet=fakultet, yonalish=yonalish, kurs=kurs, guruh=guruh, viloyat=viloyat, tuman=tuman, mfy=mfy, kocha_uy=kocha_uy, password = make_password(password1), parol=password2) 
            user.is_active = False
            user.is_staff = False
            
            return redirect('/')
    
    return render(request, 'kirish/talaba.html', {'habar':habar})


def superadmin(request):
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']        
        t_nomer = request.POST['t_nomer']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday id mavjud'  
        elif User.objects.filter(t_nomer=t_nomer):
            habar = 'Bunday telaefon nomer mavjud '         
        else:
            user = get_user_model().objects.create(lavozim='superadmin', username = username, last_name = familya, first_name = ism, t_nomer=t_nomer,password = make_password(password1), parol=password2)
            user.is_active = False
            user.is_staff = False 
            return redirect('/')          

    contex = {
        'habar':habar,
    }
    return render(request, 'kirish/superadmin.html', contex)



def dekanat(request):
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        familya = request.POST['familya']
        ism = request.POST['ism']       
        t_nomer = request.POST['t_nomer']
        dekanat_fakultet = request.POST['dekanat_fakultet']
        dekanat_kafedra = request.POST['dekanat_kafedra']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday id mavjud'
        elif User.objects.filter(t_nomer=t_nomer):
            habar = 'Bunday telaefon nomer mavjud '
        else:
            user = get_user_model().objects.create(lavozim='dekanat', username = username, last_name = familya, first_name = ism, t_nomer=t_nomer, dekanat_fakultet=dekanat_fakultet, dekanat_kafedra=dekanat_kafedra, password = make_password(password1), parol=password2)
            user.is_active = False
            user.is_staff = False 
            return redirect('/')          

    contex = {
        'habar':habar,
    }
    return render(request, 'kirish/dekanat.html', contex)

def super_admin(request):
    data = User.objects.filter(lavozim='superadmin')    
    context = {
        'data':data,
    }
    return render(request, 'adminlar/superadmin/adminlar.html', context)

def dekanat_admin(request):
    data = User.objects.filter(lavozim='dekanat')    
    context = {
        'data':data,
    }
    return render(request, 'adminlar/dekanat/adminlar.html', context)

def talabalar(request):
    data = User.objects.filter(lavozim='talaba')    
    context = {
        'data':data,
    }
    return render(request, 'adminlar/talaba/talabalar.html', context)

def dekanat_shartnoma_olgan(request):
    user = User.objects.get(pk=request.user.id)
    data = Pdf.objects.all()
    contex = {
        'data':data,
        'user':user,
    }
    return render(request, 'adminlar/dekanat/shartnoma_olgan.html', contex)


def shartnoma_olgan(request):
    data = Pdf.objects.all()
    contex = {
        'data':data,
    }
    return render(request, 'amaliyot/shartnoma_olgan.html', contex)

def adminlar(request):
    return render(request, 'adminlar/admin/adminlar.html')


# def sinov(request):
#     habar = ''
#     if request.method == 'POST':
#         kirish = request.POST['kirish']  
#         if User.objects.get(pk=request.user.id):      
#             User.objects.create(kirish=kirish)
            
#         return redirect('/kirish/')
    
#     return render(request, 'sinov.html', {'habar':habar})