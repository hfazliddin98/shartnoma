import os
import datetime as dt
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.staticfiles import finders
from reportlab.lib.pagesizes import letter
from amaliyot.models import Amaliyot
from users.models import User
from .models import Pdf, Rasm







@csrf_exempt
def qrcode(request):
    a = request.user.pk     
    
    talaba_id = User.objects.all()
    for t in talaba_id:
        import qrcode

        data = f"https://shartnoma.kspi.uz/pdf/{t.id}/"  # QR-kodga kiritmoqchi bo'lgan ma'lumot

        # QR-kod obyektini yaratish
        qr = qrcode.QRCode(version=1, box_size=10, border=4)

        # Ma'lumotni QR-kodga qo'shish
        qr.add_data(data)

        # QR-kodni yaratish
        qr.make()

        # QR-koddan tasvir yaratish
        img = qr.make_image()

        # Tasvirni saqlash
        img.save(f"media/code/qrcode{t.id}.png")
        
        link = f'https://shartnoma.kspi.uz/pdf/qrcode/{t.id}/'
        rasmlar = Rasm.objects.filter(user_id=t.id)
        
        
        media_url = '/code/'
        image_path = f'qrcode{t.id}.png'
        image_url = f'{media_url}{image_path}'
        if rasmlar:
            data = get_object_or_404(Rasm, user_id=t.id)
            data.user_id = t.id
            data.link = link 
            data.rasm = image_url
            data.save()
            print('update qilindi ')
        else:
            data = Rasm.objects.create(
                user_id = t.id,
                link = link,
                rasm = image_url
            )
            data.save()
            print('create qilindi ')
    
    template_path = 'amaliyot/qrcode.html' 
    # sayt foydalanuvchisini va amaliyotni aniq ko`rsatish uchun ishlatiladi`   
    talaba_id = request.user.id
    talaba = User.objects.get(id=talaba_id)
    amaliyot = Amaliyot.objects.get(talaba=talaba_id)
    pdf = Pdf.objects.filter(talaba_id=talaba_id)   
    qrcode = Rasm.objects.all()
    
    
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
        'qrcode':qrcode        
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # korib keyin saqlab olish
    response['Content-Disposition'] = 'filename="qrcode.pdf"'
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
def pdf(request):  
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
                    data.talaba_fakulteti = t.fakultet
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
                        talaba_fakulteti = t.fakultet, 
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
       

                
                



