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
def pdf(request, pk):  
    pdf = Pdf.objects.all()
    talaba_id = User.objects.all()
    talaba = User.objects.filter(id=pk)
    for t in talaba:
        talaba_fish = f'{t.first_name} {t.last_name} {t.sharif}'
        talaba_manzil = f'{t.viloyat} {t.tuman} {t.kocha_uy}'

    amaliyotlar = Amaliyot.objects.filter(talaba=pk)
    print('bajarildi')
    if amaliyotlar:
        for a in  amaliyotlar:  
                shifr = ''
                buyruq_raqam = '' 
                amaliyot_manzil = f'{a.viloyat_a} {a.tuman_a} {a.kocha_uy_a}'              
                talabalar = Pdf.objects.filter(talaba_id=pk)
                if talabalar:                                      
                    data = get_object_or_404(Pdf, talaba_id=pk)
                    data.talaba_f_i_sh = talaba_fish
                    data.talaba_manzil = talaba_manzil
                    data.talaba_kurs = t.kurs
                    data.talaba_shifr=shifr
                    data.talaba_fakulteti = t.fakultet
                    data.talaba_yonalishi=t.yonalish
                    data.talaba_nomer = t.t_nomer
                    data.derektor_nomer = a.d_nomeri
                    data.amaliyot_joyi=a.muassasa
                    data.amaliyot_manzili = amaliyot_manzil
                    data.amaliyot_rahbari=a.a_rahbari
                    data.biriktirilgan_rahbar=a.o_a_rahbari
                    data.amaliyot_turi=a.a_turi
                    data.amaliyot_boshlanishi=a.b_sana
                    data.amaliyot_tugashi=a.t_sana
                    data.amaliyot_buyruq_raqami=buyruq_raqam
                    data.save()                        
                    print('update qilindi  pdf')
                else:                 
                    data = Pdf.objects.create(
                        talaba_id=pk, 
                        shartnoma_raqami=a.id,
                        talaba_f_i_sh=talaba_fish, 
                        talaba_manzil = talaba_manzil, 
                        talaba_kurs=t.kurs, 
                        talaba_shifr=shifr, 
                        talaba_yonalishi=t.yonalish,
                        talaba_fakulteti = t.fakultet, 
                        talaba_nomer = t.t_nomer,
                        derektor_nomer = a.d_nomeri,
                        amaliyot_joyi=a.muassasa, 
                        amaliyot_manzili = amaliyot_manzil, 
                        amaliyot_rahbari=a.a_rahbari, 
                        biriktirilgan_rahbar=a.o_a_rahbari, 
                        amaliyot_turi=a.a_turi, 
                        amaliyot_boshlanishi=a.b_sana, 
                        amaliyot_tugashi=a.t_sana, 
                        amaliyot_buyruq_raqami=buyruq_raqam
                        )
                    data.save()
                    print('create qilindi  pdf')
        else:
            amaliyot = 'Hozirda mavjud emas'
        


 
  
    import qrcode

    data = f"https://shartnoma.kspi.uz/pdf/shartnoma/{pk}/"  # QR-kodga kiritmoqchi bo'lgan ma'lumot

        # QR-kod obyektini yaratish
    qr = qrcode.QRCode(version=1, box_size=10, border=4)

        # Ma'lumotni QR-kodga qo'shish
    qr.add_data(data)

        # QR-kodni yaratish
    qr.make()

        # QR-koddan tasvir yaratish
    img = qr.make_image()

        # Tasvirni saqlash
    img.save(f"media/code/qrcode{pk}.png")
        
    link = f'http://shartnoma.kspi.uz/media/code/qrcode{pk}.png'
    rasmlar = Rasm.objects.filter(user_id=pk)
        
        
    media_url = '/code/'
    image_path = f'qrcode{pk}.png'
    image_url = f'{media_url}{image_path}'
    if rasmlar:
            data = get_object_or_404(Rasm, user_id=pk)
            data.user_id = pk
            data.link = link 
            data.rasm = image_url
            data.save()
            print('update qilindi qr')
    else:
            data = Rasm.objects.create(
                user_id = pk,
                link = link,
                rasm = image_url
            )
            data.save()
            print('create qilindi qr')
    
            

    template_path = 'amaliyot/shartnoma.html' 
    # sayt foydalanuvchisini va amaliyotni aniq ko`rsatish uchun ishlatiladi`   
     
    pdf = Pdf.objects.filter(talaba_id=pk)
    qrcode = Rasm.objects.filter(user_id=pk)

    
    hozir = dt.datetime.now()    
    for a in amaliyotlar:
        deroktor_ismi = f'{a.d_ism}'
    
    context = {        
        'talaba':talaba,
        'deroktor_ismi':deroktor_ismi,
        'pdf':pdf,        
        'hozir':hozir,
        'qrcode':qrcode,
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
       

                
                



