# Create your models here.


from django.db import models
from datetime import datetime


# TODOs lar ile ilgili bir sınıf oluşturup içerisinde belirli tanımlamalar yapalım...

class ToDos(models.Model):
    # ToDo muzun bir başlığı olsun:
    title = models.CharField(max_length=100) # Başlığın max uzunluğu 100 karakter...
    description = models.TextField(max_length=1000, blank=True) # blank=True --->>> bu alanı boş bırakma özgürlüğü veriyor
    # title doldurulması zorunlu olan alan ama description öyle değil.
    
    # Oluşturduğumuz TODOs bitti mi bitmedi mi görebilmek için BooleanField kullanacaz...
    # yeni oluşturulduğu için "default = False" olur, yani bitmemiş olur...
    finished = models.BooleanField(default = False)

    # TODOs nun ne zaman oluşturulacağını belirlemek için DateTimeField kullanacaz.
    # Şimdi de todo nun oluşturulma zamanı ile ilgili "date" isimli bir atama yapalım
    # Oluşturduğumuz anda zamanı otomatik alabilmesi için "from datetime import datetime" deriz. 
    date = models.DateTimeField(default = datetime.now, blank=True)


# Bu yazdıklarımızı kaydettik ama bunun veri tabanına gitmesi için 
# migrate de migration u yapmamız gerekiyor (todo_project içerisinde migration u yaparız.)
# (dJangoEnv) (base) artint@artint-thinkpad:~/Desktop/n2mobil/dJangoEnv/todo_project$ python manage.py makemigrations

# -1- python manage.py makemigrations --->>> -Create model ToDos --->>> todo_app içerisinde de 0001_initial.py şeklide bir dosya oluşur.
  
  # Migrations for 'todo_app':
  # todo_app/migrations/0001_initial.py
  #   - Create model ToDos
 
  # Yani biz models.py içerisinde bir kod yazdık, bu kodlar sql komutlarına çevrilir ve tablo oluşur... 

# -2- python manage.py migrate --->>> yapınca da ... OK der. yani aktif hale gelmiştir...
  
   # Operations to perform:
     # Apply all migrations: admin, auth, contenttypes, sessions, todo_app
   # Running migrations:
    # Applying todo_app.0001_initial... OK

# Şimdi bu todo listemiz admin sayfasında görülecek. O yüzden admin.py ye gidip:
  # from.models import ToDo ---> deyip bunu admin sayfasına kabul ettirmek için de --->>> admin.site.register(ToDo) deriz.


# todo eklediğimizde "ToDo object (1)" şeklinde görülür. Ancak biz başlıklar görünsün istiyoruz. Bunun için:
    def __str__(self): # fonksiyonunu getirip,
        return self.title

# return self.name --->>> return self.title  şeklinde değiştiririz...

# database de oluşturmuş olduğumuz, todo larımız çekip Home page de gösterelim.
# öncelikle, göstereceğimiz yer views bölümü olacak. database e kaydettiğimiz todo ları views.py bölümünde çekeriz.
# Çektikten sonra da index.html de gösterme işlemi yaparız. 



