from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User


# def kirish(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             user.save()
#             return redirect('/home')
#         else:
#             messages.warning(request, 'Id yoki parol xato')
#             return redirect('/')

#     return render(request, 'kirish/login.html')


# def home(request):
#     return render(request, 'boshi/home.html')

# def royhat(request):
#     habar = ''
#     if request.method == 'POST':
#         username = request.POST['username']
#         familya = request.POST['familya']
#         ism = request.POST['ism']
#         sharif = request.POST['sharif']
#         t_yil = request.POST['t_yil']
#         yonalish = request.POST['yonalish']
#         k_yil = request.POST['k_yil']
#         viloyat = request.POST['viloyat']
#         shahar = request.POST['shahar']
#         kocha = request.POST['kocha']
#         uy_nomer = request.POST['uy_nomer']
#         telefon = request.POST['telefon']
#         familya_i = request.POST['familya_i']
#         ism_i = request.POST['ism_i']
#         sharif_i = request.POST['sharif_i']        
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         if User.objects.filter(username=username):
#             habar = 'Bunday ID mavjud'
#         elif len(telefon) < 9:
#             habar = 'Telefon nomerni kodi bilan kiriting'
#         elif User.objects.filter(telefon=telefon):
#             habar = 'Bumday telefon nomer mavjud'
#         elif len(password1) < 8 or password1 == familya or password1 == ism:
#             habar = 'Parol 8 tadan kam bolmasligi kerak'
#         elif password1 != password2:
#             habar = 'Tasdiqlash parolini to`gri kiritish'
#         else:
#             user = get_user_model().objects.create(username = username, last_name = familya, first_name = ism, sharif=sharif, t_yil=t_yil, yonalish=yonalish, k_yil=k_yil, viloyat = viloyat, shahar = shahar, kocha = kocha, uy_nomer = uy_nomer, telefon = telefon, familya_i = familya_i, ism_i = ism_i, sharif_i=sharif_i, password = make_password(password1)) 
#             user.is_active = False
#             user.is_staff = False
#             user.sana = True
#             return redirect('/')
    
#     return render(request, 'kirish/signup.html', {'habar':habar})


# def sinov(request):
#     habar = ''
#     if request.method == 'POST':
#         kirish = request.POST['kirish']  
#         if User.objects.get(pk=request.user.id):      
#             User.objects.create(kirish=kirish)
            
#         return redirect('/kirish/')
    
#     return render(request, 'sinov.html', {'habar':habar})