from django.contrib import admin

from kozyap.models import Staff, Object, Brigadier, StaffReport, ToDoList, Intruments
from kozyap_site.models import About, Gallery, GalleryCategory, Partner, ContactForm

admin.site.register(Staff)
admin.site.register(Object)
admin.site.register(Brigadier)
admin.site.register(StaffReport)
admin.site.register(ToDoList)
admin.site.register(Intruments)
admin.site.register(About)
admin.site.register(Gallery)
admin.site.register(GalleryCategory)
admin.site.register(Partner)
admin.site.register(ContactForm)
