from django.shortcuts import render, redirect
from .models import Amaliyot

def amaliyot(request):
    habar = ''
    if request.method == 'POST':
        viloyat_a = request.POST['viloyat_a']
        tuman_a = request.POST['tuman_a']
        mfy_a = request.POST['mfy_a']
        kocha_uy_a = request.POST['kocha_uy_a']
        muassasa = request.POST['muassasa']
        d_ism = request.POST['d_ism']
        d_nomeri = request.POST['d_nomeri']
        kurs = request.POST['kurs']
        a_rahbari = request.POST['a_rahbari']
        o_a_rahbari = request.POST['o_a_rahbari']
        a_turi = request.POST['a_turi']
        b_sana = request.POST['b_sana']
        t_sana = request.POST['t_sana']           
        
        Amaliyot.objects.create(viloyat_a = viloyat_a, tuman_a = tuman_a, mfy_a = mfy_a, kocha_uy_a=kocha_uy_a, muassasa=muassasa, d_ism=d_ism, d_nomeri=d_nomeri, b_sana=b_sana, a_rahbari=a_rahbari, o_a_rahbari=o_a_rahbari, a_turi=a_turi, kurs=kurs, t_sana=t_sana) 
        return redirect('/') 
    
    contex = {
        'habar':habar,
    }     
    return render(request, 'amaliyot/amaliyot.html', contex)