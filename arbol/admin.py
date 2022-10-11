from django.contrib import admin
from .models import Arbol
from .models import Predio
from .models import direccion
from .models import foto
from .models import tipoArbol

class ArbolAdmin(admin.ModelAdmin):
    list_display = ("nombre","tipo","codigoArbol")
admin.site.register(tipoArbol)
admin.site.register(foto)
admin.site.register(Predio)
admin.site.register(direccion)
admin.site.register(Arbol,ArbolAdmin)

# Register your models here.
