import os
import xlwt
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
    talaba = User.objects.filter(id=pk)
    for t in talaba:
        talaba_fish = f'{t.first_name} {t.last_name} {t.sharif}'
        talaba_manzil = f'{t.viloyat} {t.tuman} {t.kocha_uy}'

    amaliyotlar = Amaliyot.objects.filter(talaba=pk)
    if amaliyotlar:
        for a in  amaliyotlar:  
                shifr = ''
                buyruq_raqam = f'{a.d_ism} tel:{a.d_nomeri}'
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
                    data.amaliyot_tugashi=t.talim_turi
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
                        amaliyot_tugashi=t.talim_turi, 
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
     
    # pdf = Pdf.objects.filter(talaba_id=pk)
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
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="shartnoma.pdf"'
#   


    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
       return HttpResponse("Bizda ba'zi xatolar bor edi " + html + " serverda texnik ish lar olib borilmoqda !!!")
    return response


@csrf_exempt
def malumot_csv(request):
    # content-type of response
        response = HttpResponse(content_type='application/ms-excel')

        #decide file name
        response['Content-Disposition'] = 'attachment; filename="arizalar.xls"'

        #creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        #adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        #column header names, you can use your own headers here
        columns = [
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
            'Talim turi',
            'Muassasa rahbari va tel nomeri',                 
        ]

        #write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        #get your data, from database or from a text file...
        shartnomalar = Pdf.objects.all()
        if shartnomalar:            
            for my_row in shartnomalar:                
                row_num = row_num + 1
                ws.write(row_num, 0, my_row.shartnoma_raqami, font_style)
                ws.write(row_num, 1, my_row.talaba_f_i_sh, font_style)
                ws.write(row_num, 2, my_row.talaba_manzil, font_style)
                ws.write(row_num, 3, my_row.talaba_kurs, font_style)
                ws.write(row_num, 4, my_row.talaba_shifr, font_style)
                ws.write(row_num, 5, my_row.talaba_yonalishi, font_style)
                ws.write(row_num, 6, my_row.amaliyot_joyi, font_style)
                ws.write(row_num, 7, my_row.amaliyot_manzili, font_style)
                ws.write(row_num, 8, my_row.amaliyot_rahbari, font_style)
                ws.write(row_num, 9, my_row.biriktirilgan_rahbar, font_style)
                ws.write(row_num, 10, my_row.amaliyot_turi, font_style)
                ws.write(row_num, 11, my_row.amaliyot_boshlanishi, font_style)
                ws.write(row_num, 12, my_row.amaliyot_tugashi, font_style)
                ws.write(row_num, 13, my_row.amaliyot_buyruq_raqami, font_style)               

            wb.save(response)
            return response
        else:
            return redirect('/shartnoma_olgan/')
        
   
   
@csrf_exempt
def dekanat_csv(request):
        # content-type of response
        response = HttpResponse(content_type='application/ms-excel')

        #decide file name
        response['Content-Disposition'] = 'attachment; filename="arizalar.xls"'

        #creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        #adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        #column header names, you can use your own headers here
        columns = [
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
            'Muassasa rahbari va tel nomeri',                    
        ]

        #write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        #get your data, from database or from a text file...
        fakultet = request.user.dekanat_fakultet
        print(fakultet)
        print(Pdf.objects.filter(talaba_fakulteti=fakultet))
        shartnomalar = Pdf.objects.filter(talaba_fakulteti=fakultet)
        if shartnomalar:            
            for my_row in shartnomalar:                
                row_num = row_num + 1
                ws.write(row_num, 0, my_row.shartnoma_raqami, font_style)
                ws.write(row_num, 1, my_row.talaba_f_i_sh, font_style)
                ws.write(row_num, 2, my_row.talaba_manzil, font_style)
                ws.write(row_num, 3, my_row.talaba_kurs, font_style)
                ws.write(row_num, 4, my_row.talaba_shifr, font_style)
                ws.write(row_num, 5, my_row.talaba_yonalishi, font_style)
                ws.write(row_num, 6, my_row.amaliyot_joyi, font_style)
                ws.write(row_num, 7, my_row.amaliyot_manzili, font_style)
                ws.write(row_num, 8, my_row.amaliyot_rahbari, font_style)
                ws.write(row_num, 9, my_row.biriktirilgan_rahbar, font_style)
                ws.write(row_num, 10, my_row.amaliyot_turi, font_style)
                ws.write(row_num, 11, my_row.amaliyot_boshlanishi, font_style)
                ws.write(row_num, 12, my_row.amaliyot_tugashi, font_style)
                ws.write(row_num, 13, my_row.amaliyot_buyruq_raqami, font_style)               

            wb.save(response)
            return response
        else:
            return redirect('/dekanat_shartnoma_olgan/')
        


@csrf_exempt
def qoshimcha(request):


     return render(request, 'adminlar/superadmin/qoshimcha.html')


@csrf_exempt
def qoshimcha_csv(request):     
     amaliyot = Amaliyot.objects.all()

     return HttpResponse('Bajarildi')

@csrf_exempt
def botirov_pdf(request):
    try:
        template_path = 'pdf.html' 
        context = {        
       
        }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="shartnoma.pdf"'   


        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse("Bizda ba'zi xatolar bor edi " + html + " serverda texnik ish lar olib borilmoqda !!!")
        return response
    except:       

        
        return HttpResponse('Malumot yuborilmadi !!!')

                
                



