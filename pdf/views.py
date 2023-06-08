import os
import datetime as dt
from   django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
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


@csrf_exempt
def pdf(request):   
    template_path = 'amaliyot/shartnoma.html' 
    # sayt foydalanuvchisini va amaliyotni aniq ko`rsatish uchun ishlatiladi`   
    talaba_id = request.user.id
    talaba = User.objects.get(id=talaba_id)
    amaliyot = Amaliyot.objects.get(talaba=talaba_id)
    pdf = Pdf.objects.filter(talaba_id=talaba_id)
    
    hozir = dt.datetime.now()
    yil = hozir.year
    oy = hozir.month
    kun = hozir.day
    
    context = {        
        'talaba':talaba,
        'amaliyot':amaliyot,
        'pdf':pdf,
        'yil':yil,
        'oy':oy,
        'kun':kun,
        'hozir':hozir,
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


@csrf_exempt
def malumot_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=talabalar.csv'

    writer = csv.writer(response)
    
    
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
    

    talabalar = User.objects.all()
    for t in talabalar:             
        shartnoma = Pdf.objects.filter(talaba_id=t.id)
        if shartnoma:            
            for s in shartnoma:               
                print(s.talaba_id)
                print(t.id)
                print(s.amaliyot_buyruq_raqami)              
                 
            
                writer.writerow([
                    s.shartnoma_raqami,
                    s.talaba_f_i_sh,
                    s.talaba_manzil,
                    s.talaba_kurs,
                    s.talaba_shifr,
                    s.talaba_yonalishi,
                    s.amaliyot_joyi,
                    s.amaliyot_manzili,
                    s.amaliyot_rahbari,
                    s.biriktirilgan_rahbar,
                    s.amaliyot_turi,
                    s.amaliyot_boshlanishi,
                    s.amaliyot_tugashi,
                    s.amaliyot_buyruq_raqami
                ])

    return response


@csrf_exempt
def dekanat_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=talabalar.csv'

    writer = csv.writer(response)
    
    
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
    
    fakultet = request.user.dekanat_fakultet
    talabalar = User.objects.filter(fakultet=fakultet)
    for t in talabalar:             
        shartnoma = Pdf.objects.filter(talaba_id=t.id)
        if shartnoma:            
            for s in shartnoma:               
                print(s.talaba_id)
                print(t.id)
                print(s.amaliyot_buyruq_raqami)              
                 
            
                writer.writerow([
                    s.shartnoma_raqami,
                    s.talaba_f_i_sh,
                    s.talaba_manzil,
                    s.talaba_kurs,
                    s.talaba_shifr,
                    s.talaba_yonalishi,
                    s.amaliyot_joyi,
                    s.amaliyot_manzili,
                    s.amaliyot_rahbari,
                    s.biriktirilgan_rahbar,
                    s.amaliyot_turi,
                    s.amaliyot_boshlanishi,
                    s.amaliyot_tugashi,
                    s.amaliyot_buyruq_raqami
                ])

    return response
       

                
                



