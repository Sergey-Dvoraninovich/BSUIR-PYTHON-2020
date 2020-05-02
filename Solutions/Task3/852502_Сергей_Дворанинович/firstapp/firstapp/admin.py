from django.contrib import admin
from .models import New_Archi
from .models import New_Style
from .models import New_Building
from .models import new_Building_photo
from .models import Test_User_Info
from .models import My_New_User_Comment

# Register your models here.

admin.site.register(New_Archi)
admin.site.register(New_Style)
admin.site.register(New_Building)
admin.site.register(new_Building_photo)
admin.site.register(Test_User_Info)
admin.site.register(My_New_User_Comment)





#from .models import Person
#from .models import Test
#from .models import New_User
#from .models import New_User_Building_Comment
#from .models import Test_User_Comment
#admin.site.register(Person)
#admin.site.register(Test)
#admin.site.register(New_User_Building_Comment)
#admin.site.register(New_User)
#admin.site.register(Test_User_Comment)