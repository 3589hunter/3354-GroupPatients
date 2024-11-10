# Generated by Django 4.1.6 on 2023-04-14 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='doc_dep',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.departments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctors',
            name='doc_name',
            field=models.CharField(max_length=255),
        ),
    ]
