from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from .models import Amaliyot


@csrf_exempt
def amaliyotlar(request):
    userlar = User.objects.all()
    user = request.user.id
    habar = ''
    if request.method == 'POST':
        viloyat_a = request.POST['viloyat_a']
        tuman_a = request.POST['tuman_a']        
        kocha_uy_a = request.POST['kocha_uy_a']
        muassasa = request.POST['muassasa']
        d_ism = request.POST['d_ism']
        d_nomeri = request.POST['d_nomeri']
        kurs = request.POST['kurs']
        a_rahbari = request.POST['a_rahbari']
        o_a_rahbari = request.POST['o_a_rahbari']
        a_turi = request.POST['a_turi']
               
        if Amaliyot.objects.filter(talaba=user):
            habar = 'Sizga shartnoma berilgan yangilashingiz munkun'   
        else:        
            Amaliyot.objects.create(talaba=user, viloyat_a=viloyat_a,tuman_a=tuman_a, kocha_uy_a=kocha_uy_a, muassasa=muassasa, d_ism=d_ism, d_nomeri=d_nomeri, kurs=kurs, a_rahbari=a_rahbari, o_a_rahbari=o_a_rahbari, a_turi=a_turi) 
            return redirect('/') 
    
    contex = {
        'userlar':userlar,
        'user':user,
        'habar':habar,
    }     
    return render(request, 'amaliyot/amaliyot.html', contex)


@csrf_exempt
def update_amaliyot(request, pk):
    data = get_object_or_404(Amaliyot, pk=pk)    
    if request.method == 'POST':
        viloyat_a = request.POST['viloyat_a']
        tuman_a = request.POST['tuman_a']        
        kocha_uy_a = request.POST['kocha_uy_a']
        muassasa = request.POST['muassasa']
        d_ism = request.POST['d_ism']
        d_nomeri = request.POST['d_nomeri']
        kurs = request.POST['kurs']
        a_rahbari = request.POST['a_rahbari']
        o_a_rahbari = request.POST['o_a_rahbari']
        a_turi = request.POST['a_turi']  
            

        data.viloyat_a = viloyat_a
        data.tuman_a = tuman_a        
        kocha_uy_a = kocha_uy_a
        data.muassasa = muassasa
        data.d_ism = d_ism
        data.d_nomeri = d_nomeri
        data.kurs = kurs
        data.a_rahbari = a_rahbari
        data.o_a_rahbari = o_a_rahbari
        data.a_turi = a_turi        
        data.save()
        return redirect('/', pk=data.id)


    contex = {
       
    }
    return render(request, 'amaliyot/update_amaliyot.html', contex)
