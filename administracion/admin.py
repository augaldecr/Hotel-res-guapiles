from django.contrib import admin
from .models import Hotel, Habitacion, Persona, Consumo, Extra


class ConsumoAdmin(admin.ModelAdmin):
	list_display = ('id','fecha', 'habitacion', 'persona', 'aprobada')
	list_editable = ('id','fecha', 'habitacion', 'persona',  'aprobada')
	list_filter = ('id','fecha', 'habitacion', 'persona',  'aprobada')
	search_fields = ('id','fecha', 'habitacion', 'persona', 'aprobada')


class PersonaAdmin(admin.ModelAdmin):
	list_display = ('id', 'correo', 'nombre', 'apellido1', 'apellido2', 'telefono')
	list_editable = ('id', 'correo', 'nombre', 'apellido1', 'apellido2', 'telefono')
	list_filter = ('id', 'correo', 'nombre', 'apellido1', 'apellido2', 'telefono')
	search_fields = ('id', 'correo', 'nombre', 'apellido1', 'apellido2', 'telefono')


class HabitacionAdmin(admin.ModelAdmin):
	list_display = ('id', 'numero', 'localizacion', 'precioBase', 'hotel')
	list_editable = ('id', 'numero', 'localizacion', 'precioBase', 'hotel')
	list_filter = ('id', 'numero', 'localizacion', 'precioBase', 'hotel')
	search_fields = ('id', 'numero', 'localizacion', 'precioBase', 'hotel')


class ExtraAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'precio')
	list_editable = ('id','nombre', 'precio')
	list_filter = ('id','nombre', 'precio')
	search_fields = ('id','nombre', 'precio')


admin.site.register(Hotel)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Consumo, ConsumoAdmin)
admin.site.register(Extra, ExtraAdmin)


#TODO: Facturacion
