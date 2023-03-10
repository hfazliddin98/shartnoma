# https://arm2022.herokuapp.com/ | https://git.heroku.com/arm2022.git

#  superuserlar
#  username  clay
#  passwod   hfazliddin98

#  userlar
#  username  arm_(1,2,3,4)
#  passwod   arm#202(1,2,3,4)


# pip orqali pipenv ni ornatib olamiz
# pip3 install pipenv==2022.5.2

# pipenv orqali django ni rnatib olamiz
# pipenv install django==4.0.4

# djangoda loyihani yaratish uchun va asosiy boshqaruv appining nomini kiritish buyrugi
# django-admin startproject <loyiha nomi 'asosiy bosshqaruv panali hisoblanadi'>

# djangoga yangi app yaratish uchun
# python manage.py startapp <app nomi>

# modelga yangiliklarni qoshishish uchun migratsiya qilinadi
# python manage.py makemigrations <app nomi>
# python manage.py migrate

# loyihaga super user kiritish uchun
# python manage.py createsuperuser

# loyihani ishga tushrish uchun
# python manage.py runserver

#malumotlarni qabul qilish uchun
# pipenv install requests==2.28.1
# pipenv install render==1.0.0


# deploy qilish uchun paketlar muhitdan tashqarida o`rnatiladi

# pipenv install environs==9.5.0
# malumotlar bazasini o`rnatish jarayoni uchun
# pipenv install psycopg2-binary
# static fayillarni serverda korsatish uchun
# pipenv install whitenoise==6.2.0

# herokuga tayorlash
# pipenv install gunicorn==20.1.0
