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

# def malumot_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=talabalar.csv'

#     writer = csv.writer(response)

#     talabalar = User.objects.all()
#     for t in talabalar:
#         t.id
#         print(t.id)
#     amaliyotlar = Amaliyot.objects.all()

#     writer.writerow([
#         'Ism',
#         'Familya',
#         'Sharif',
#         'Kursi',
#         'Guruhi',
#         'Yo`nalish, mutahasislik nomi',
#         'O`qish smetasi(grand yoki kontrak)',
#         'O`qishga kirgan buyruq raqami va sanasi',
#         'O`qishni boshqa OTM dan ko`chirilgan, tiklagan yoki akadem ta`tilda qaytgan buyruq raqami sanasi',
#         'Reting (baholash) daftarchasining raqami',
#         'Pasport malumoti bo`yicha millati',
#         'Pasport malumoti bo`yicha jinsi',
#         'Pasport malumoti bo`yicha tug`lgan yili',
#         'Pasport malumoti bo`yicha tug`ilgan oy',
#         'Pasport malumoti bo`yicha tug`ilgan kun',
#         'Pasport malumoti bo`yicha tug`lgan viloyati',
#         'Pasport malumoti bo`yicha tug`lgan (shahar, tuman)',
#         'Pasport malumoti bo`yicha yashash joyi viloyati',
#         'Pasport malumoti bo`yicha yashash joyi (shahar, tuman)',
#         'Pasport malumoti bo`yicha yashash joyi (ko`cha, qishlog`i)',
#         'Pasport malumoti bo`yicha yashash joyi uy raqami',
#         'Pasport seryasi',
#         'Pasport raqami',
#         'Pasport JSHR raqami',
#         'Harbiy qism tafsiyanomasiga egami (ega bo`lsa QK yozilsin)',
#         'Harbiy qisimni tugatgan yili',
#         'Vaqtincha ijaradagi turar joyi manzili (talabalar uyi)',
#         'Vaqtincha ijaradagi turar joyi manzili (shahar, tuman)',
#         'Vaqtincha ijaradagi turar joyi manzili (ko`cha qishlog`i)',
#         'Vaqtincha ijaradagi turar joyi manzili (uy raqami)',
#         'Ijtimoiy holati',
#         'Nogironligi (guruhi)',
#         'Nogironligi (guruhi) FTEK raqami, qachon berilgan',
#         'Oilaviy ahvoni',
#         'Farzandlar soni',
#         'Talabaning telefon raqami',
#         'Talabaning ish joyini kiriting',
#         'Talabaning ish joyi manzilini kiriting',
#         'Otasining ismi',
#         'Otasining familyasi',
#         'Otasining sharifi',
#         'Otasining lavozimi',
#         'Otasining ish joyi nomi, manzili ',
#         'Otasining telefon raqami',
#         'Onasining ismi',
#         'Onasining familyasi',
#         'Onasining sharifi',
#         'Onasining lavozimi',
#         'Onasining ish joyi nomi, manzili',
#         'Onasining telefon raqami',
#         'Tyutrning ismi',
#         'Tyutrning familyasi',
#         'Tyutrning sharifi',           
#         'Tyutrning telefon raqami',
#     ])

#     for talaba in talabalar:
#         writer.writerow([
#             talaba.ism,
#             talaba.familya,
#             talaba.sharif,
#             talaba.kurs,
#             talaba.guruh,
#             talaba.yonalish,
#             talaba.smeta,
#             talaba.raqam,
#             talaba.tatil,
#             talaba.reting,            
#             talaba.millat,
#             talaba.jinsi,
#             talaba.t_yil,
#             talaba.t_oy,
#             talaba.t_kun,
#             talaba.t_viloyat,
#             talaba.t_tuman,
#             talaba.p_viloyat,
#             talaba.p_tuman,
#             talaba.p_kocha,
#             talaba.p_uy,
#             talaba.p_serya,
#             talaba.p_raqam,
#             talaba.p_jshr,
#             talaba.tavsiyanoma,
#             talaba.qism,
#             talaba.talaba_uy,
#             talaba.tuman,
#             talaba.kocha,
#             talaba.raqam,
#             talaba.ijtimoiy,
#             talaba.nogironligi,
#             talaba.nogironligi_ftek,
#             talaba.ahvoli,
#             talaba.soni,
#             talaba.telefon,
#             talaba.talaba_ish,
#             talaba.talaba_manzil,
#             talaba.ota_ism,
#             talaba.ota_familya,
#             talaba.ota_sharif,
#             talaba.ota_lavozim,
#             talaba.ota_manzil,
#             talaba.ota_telefon,
#             talaba.ona_ism,
#             talaba.ona_familya,
#             talaba.ona_sharif,
#             talaba.ona_lavozim,
#             talaba.ona_manzil,
#             talaba.ona_telefon,
#             talaba.tyutr_ism,
#             talaba.tyutr_familya,
#             talaba.tyutr_sharif,         
#             talaba.tyutr_telefon,
#         ])

#     return response



