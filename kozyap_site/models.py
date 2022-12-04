from django.core.validators import RegexValidator
from django.db.models import Model, DateTimeField, TextField, CharField, ImageField, DateField, FloatField, ForeignKey, \
    CASCADE


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Service(BaseModel):
    title = CharField(verbose_name="Sarlavha", max_length=255)
    description = TextField(verbose_name="Malumot")
    image = ImageField(verbose_name="Rasm", upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Servis"
        verbose_name_plural = "Servis"


class About(BaseModel):
    title = CharField(verbose_name='Sarlavha', max_length=255)
    description = TextField(verbose_name='Malumot')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'about'
        verbose_name = "Biz Haqimizda"
        verbose_name_plural = "Biz Haqimizda"


class Partner(BaseModel):
    image = ImageField(verbose_name="Rasmi", upload_to='images/')
    title = CharField(verbose_name="Nomi", max_length=30, null=True, blank=True)
    little_desc = CharField(verbose_name="Bafurcha Malumot", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'partner'
        verbose_name = 'Hamkorlar'
        verbose_name_plural = "Hamkorlarimiz"


class GalleryCategory(BaseModel):
    title = CharField(verbose_name="Nomi", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'gal_category'
        verbose_name = "Galeriya Kategoriyasi"
        verbose_name_plural = 'Galeriya Kategoriyasi'


class Gallery(BaseModel):
    image = ImageField(verbose_name="Rasmi", upload_to='images/')
    category = ForeignKey(verbose_name="Kategoriyasi", to=GalleryCategory, on_delete=CASCADE)
    title = CharField(verbose_name="Nomi", max_length=30, null=True, blank=True)
    little_desc = CharField(verbose_name="Bafurcha Malumot", max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'gallery'
        verbose_name = 'Galleriya'
        verbose_name_plural = 'Galleriya'


class Reference(Model):
    title = CharField(verbose_name="Nomi", max_length=255)
    start_date = DateField(verbose_name="Boshlangan Vaqti")
    end_date = DateField(verbose_name="Tugagan Vaqti")
    object = CharField(verbose_name='Manzil', max_length=255)
    m2_quad = FloatField(verbose_name='M2')
    casting = CharField(verbose_name="Kasting shakli", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "referenslar"
        verbose_name = "Referenslar"
        verbose_name_plural = "Referenslar"


class ContactForm(BaseModel):
    phone_regex = RegexValidator(regex=r'^998[0-9]{2}[0-9]{7}$', message='Faqat Ozbekiston Raqami Bolish kerak')
    first_name = CharField(verbose_name="Ismi", max_length=255)
    last_name = CharField(verbose_name="Familiyasi", max_length=255)
    phone_number = CharField(verbose_name="Nomeri", validators=[phone_regex], max_length=13)
    message = TextField(verbose_name="Matni")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = "contact"
        verbose_name = "Kontaktdan"
        verbose_name_plural = "Kontakdan"


from django.db import models

# Create your models here.
