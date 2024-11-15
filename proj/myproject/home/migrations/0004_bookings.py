# Generated by Django 4.1.6 on 2023-04-18 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_doctors_doc_dep_alter_doctors_doc_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_phone', models.CharField(max_length=12)),
                ('p_email', models.EmailField(max_length=254)),
                ('Booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctors')),
            ],
        ),
    ]
