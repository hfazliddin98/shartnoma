import os
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
        'Amaliyot bo`yicha buyruq raqami, sanasi'                    
    ])  
    talabalar = Pdf.objects.all()
    for t in talabalar:
         
            
        writer.writerow([
            t.shartnoma_raqami,
            t.talaba_f_i_sh,
            t.talaba_manzil,
            t.talaba_kurs,
            t.talaba_shifr,
            t.talaba_yonalishi,
            t.amaliyot_joyi,
            t.amaliyot_manzili,
            t.amaliyot_rahbari,
            t.biriktirilgan_rahbar,
            t.amaliyot_turi,
            t.amaliyot_boshlanishi,
            t.amaliyot_tugashi,
            t.amaliyot_buyruq_raqami
        ])

    return response
       

                
                



