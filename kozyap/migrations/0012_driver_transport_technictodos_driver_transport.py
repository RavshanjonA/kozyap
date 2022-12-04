# Generated by Django 4.1.3 on 2022-11-27 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('kozyap', '0002_object_brigadier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128, verbose_name='Ism Familya')),
                ('username', models.CharField(max_length=56, verbose_name='Telegram Username')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon Raqam')),
                ('tgid', models.IntegerField(verbose_name='Telegram ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Mashina Nomi')),
                ('number', models.CharField(max_length=128, verbose_name='Mashina Raqami')),
                ('company', models.CharField(max_length=128, verbose_name='Mashina Raqami')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicTodos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Sana')),
                ('todos', models.CharField(max_length=256, verbose_name='Nima Ish Qildi')),
                ('driver', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT,
                                             related_name='techtodos', to='kozyap.driver',
                                             verbose_name='Texnika Mashinisti')),
                ('object', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT,
                                             related_name='techtodos', to='kozyap.object',
                                             verbose_name='Texnika Nomi')),
                ('transport', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT,
                                                related_name='techtodos', to='kozyap.transport',
                                                verbose_name='Texnika Nomi')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='transport',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='kozyap.transport',
                                    verbose_name='Mashinasi'),
        ),
    ]