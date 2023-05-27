import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import csv
from django.contrib.staticfiles import finders
from reportlab.lib.pagesizes import letter
from amaliyot.models import Amaliyot
from users.models import User
from .models import Pdf



def shartnoma(request):    
    talaba_id = User.objects.all()
    def qaytar():
        talaba_id = User.objects.all()
        for t in talaba_id:
            amaliyotlar = Amaliyot.objects.filter(talaba=t.id)
            if amaliyotlar:
                amaliyot = amaliyotlar
        return amaliyot
    def talaba():
        t = request.user.id
        return t    
    print(f'qaytaryapti {qaytar()}')
    print(f'talaba {talaba()}')
    # data = Pdf.objects.create(talaba_id=[lambda :t for t in talaba_id], amaliyot_id='a')
    # data.save()    
    # for t in talaba_id:
    #     amaliyotlar = Amaliyot.objects.filter(talaba=t)
    #     for a in amaliyotlar:
    #         print(f'salom {a}')
            

    contex = {

    }
    return render(request, 'sinov.html', contex)




def pdf(request):   
    template_path = 'amaliyot/shartnoma.html' 
    # sayt foydalanuvchisini va amaliyotni aniq ko`rsatish uchun ishlatiladi`   
    talaba_id = request.user.id
    talaba = User.objects.get(id=talaba_id)
    amaliyot = Amaliyot.objects.get(talaba=talaba_id)
    
    context = {        
        'talaba':talaba,
        'amaliyot':amaliyot,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # korib keyin saqlab olish
    response['Content-Disposition'] = 'filename="shartnoma.pdf"'
#     avto saqlab olish
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse("Bizda ba'zi xatolar bor edi " + html + " serverda texnik ish lar olib borilmoqda !!!")
    return response

def malumot_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=talabalar.csv'

    writer = csv.writer(response)
    

    talabalar = User.objects.all()
    for t in talabalar:
             
        amaliyotlar = Amaliyot.objects.filter(talaba=t.id)
        if amaliyotlar:
            amaliyot = amaliyotlar
            for a in amaliyot:
                talaba = f'{t.first_name} {t.last_name} {t.sharif}'
                print(a.talaba)
                print(t.id)

                
                writer.writerow([
                    'Shartnoma raqami',
                    'Talaba F.I.SH',
                    'Talabaning yashash manzili',
                    'Kursi',
                    'Talaba yo`nalish shifri',
                    'Talaba yo`nalish nomi',
                    'Amaliyot o`tash joyi (korxona, tashkilot)ning nomi',
                    'Amaliyot o`tash joyi (korxona, tashkilot)ning manzili',
                    'Amaliyot o`tash joyi (korxona, tashkilot)dagi amaliyot rahbari',
                    'OTMdan biriktirilgan amaliyot rahbari F.I.SH',
                    'Amaliyot turi',
                    'Amaliyotning boshlanish muddati',
                    'Amaliyotning tugash muddati',
                    'Amaliyot bo`yicha buyruq raqami, sanasi',
                    
                ])    
            
                writer.writerow([
                    t.id,
                    talaba,
                    # talaba.familya,
                    # talaba.sharif,
                    # talaba.kurs,
                    # talaba.guruh,
                    # talaba.yonalish,
                    # talaba.smeta,
                    # talaba.raqam,
                    # talaba.tatil,
                    # talaba.reting,            
                    # talaba.millat,
                    # talaba.jinsi,
                    # talaba.t_yil,
                    # talaba.t_oy,
                    # talaba.t_kun,
                    # talaba.t_viloyat,
                    # talaba.t_tuman,
                    # talaba.p_viloyat,
                    # talaba.p_tuman,
                    # talaba.p_kocha,
                    # talaba.p_uy,
                    # talaba.p_serya,
                    # talaba.p_raqam,
                    # talaba.p_jshr,
                    # talaba.tavsiyanoma,
                    # talaba.qism,
                    # talaba.talaba_uy,
                    # talaba.tuman,
                    # talaba.kocha,
                    # talaba.raqam,
                    # talaba.ijtimoiy,
                    # talaba.nogironligi,
                    # talaba.nogironligi_ftek,
                    # talaba.ahvoli,
                    # talaba.soni,
                    # talaba.telefon,
                    # talaba.talaba_ish,
                    # talaba.talaba_manzil,
                    # talaba.ota_ism,
                    # talaba.ota_familya,
                    # talaba.ota_sharif,
                    # talaba.ota_lavozim,
                    # talaba.ota_manzil,
                    # talaba.ota_telefon,
                    # talaba.ona_ism,
                    # talaba.ona_familya,
                    # talaba.ona_sharif,
                    # talaba.ona_lavozim,
                    # talaba.ona_manzil,
                    # talaba.ona_telefon,
                    # talaba.tyutr_ism,
                    # talaba.tyutr_familya,
                    # talaba.tyutr_sharif,         
                    # talaba.tyutr_telefon,
                ])

    return response



