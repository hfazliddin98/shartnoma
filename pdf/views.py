import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from reportlab.lib.pagesizes import letter
from .models import Oliy_yurt, Ish
from users.models import User








     

# Create your views here.
def pdf(request):
    template_path = 'test.html' 
    # sayt foydalanuvchisini aniq ko`rsatish uchun ishlatiladi`   
    foydalanuvchi = User.objects.get(pk=request.user.id)
    
    
    context = {'myvar': 'Qo`qon davlat pedagokika instituti' , 'userlar': foydalanuvchi,}
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
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse("Bizda ba'zi xatolar bor edi " + html + " serverda texnik ish lar olib borilmoqda !!!")
    return response




