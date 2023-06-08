from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User
from amaliyot.models import Amaliyot
from pdf.models import Pdf

@csrf_exempt
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

@csrf_exempt
def home(request):
    talaba = request.user.id
    userlar = User.objects.all()
    amaliyotlar = Amaliyot.objects.filter(talaba=talaba)
    contex = {
        'userlar': userlar,
        'amaliyotlar':amaliyotlar,
        'talaba':talaba,
    }
    return render(request, 'boshi/home.html', contex)

@csrf_exempt
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



@csrf_exempt
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


@csrf_exempt
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

@csrf_exempt
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


@csrf_exempt
def talabalar(request):
    data = User.objects.filter(lavozim='talaba') 
    talaba = Pdf.objects.all()   
    context = {
        'data':data,
        'talaba':talaba,
    }
    return render(request, 'adminlar/talaba/talabalar.html', context)



@csrf_exempt
def dekanat_talaba(request):
    fakultet = request.user.dekanat_fakultet
    talaba = User.objects.filter(fakultet=fakultet)
    contex = {
        'talaba':talaba,        
    }
    return render(request, 'adminlar/dekanat/talaba.html', contex)



@csrf_exempt
def dekanat_shartnoma_olgan(request):
    fakultet = request.user.dekanat_fakultet
    talabalar = User.objects.filter(fakultet=fakultet)
    for t in talabalar:             
        shartnoma = Pdf.objects.filter(talaba_id=t.id)
    
    
    contex = {
        'shartnoma':shartnoma,       
    }
    return render(request, 'adminlar/dekanat/shartnoma_olgan.html', contex)



@csrf_exempt
def shartnoma_olgan(request):
    pdf = Pdf.objects.all()
    talaba_id = User.objects.all()
    for t in talaba_id:
        amaliyotlar = Amaliyot.objects.filter(talaba=t.id)
        if amaliyotlar:
            for a in  amaliyotlar:  
                shifr = ''
                buyruq_raqam = ''             
                talabalar = Pdf.objects.filter(talaba_id=t.id)
                if talabalar:
                    # update qilyapti
                    talaba = f'{t.first_name} {t.last_name} {t.sharif}'                        
                    data = get_object_or_404(Pdf, talaba_id=t.id)
                    data.talaba_f_i_sh = talaba
                    data.talaba_manzil = t.tuman
                    data.talaba_kurs = t.kurs
                    data.talaba_shifr=shifr
                    data.talaba_yonalishi=t.yonalish
                    data.amaliyot_joyi=a.muassasa
                    data.amaliyot_manzili=a.tuman_a
                    data.amaliyot_rahbari=a.a_rahbari
                    data.biriktirilgan_rahbar=a.o_a_rahbari
                    data.amaliyot_turi=a.a_turi
                    data.amaliyot_boshlanishi=a.b_sana
                    data.amaliyot_tugashi=a.t_sana
                    data.amaliyot_buyruq_raqami=buyruq_raqam
                    data.save()                        
                    print('update qilindi ')
                else:
                    # create qilyapti                    
                    shifr = ''
                    buyruq_raqam = ''
                    talaba= f'{t.first_name} {t.last_name} {t.sharif}'
                    data = Pdf.objects.create(
                        talaba_id=t.id, 
                        shartnoma_raqami=a.id,
                        talaba_f_i_sh=talaba, 
                        talaba_manzil=t.tuman, 
                        talaba_kurs=t.kurs, 
                        talaba_shifr=shifr, 
                        talaba_yonalishi=t.yonalish, 
                        amaliyot_joyi=a.muassasa, 
                        amaliyot_manzili=a.tuman_a, 
                        amaliyot_rahbari=a.a_rahbari, 
                        biriktirilgan_rahbar=a.o_a_rahbari, 
                        amaliyot_turi=a.a_turi, 
                        amaliyot_boshlanishi=a.b_sana, 
                        amaliyot_tugashi=a.t_sana, 
                        amaliyot_buyruq_raqami=buyruq_raqam
                        )
                    data.save()
                    print('create qilindi ')
        else:
            amaliyot = 'Hozirda mavjud emas'
     
          

    contex = {
        'pdf':pdf,
        'amaliyot':amaliyot,
    }
    return render(request, 'amaliyot/shartnoma_olgan.html', contex)


@csrf_exempt
def adminlar(request):
    return render(request, 'adminlar/admin/adminlar.html')


