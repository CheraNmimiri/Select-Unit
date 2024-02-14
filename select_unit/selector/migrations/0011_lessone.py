# Generated by Django 5.0.2 on 2024-02-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selector', '0010_alter_student_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('unit', models.IntegerField()),
                ('professor', models.CharField(max_length=250)),
                ('College', models.CharField(choices=[('eng', 'engineering'), ('hum', 'Humanities'), ('med', 'Medical')], max_length=50)),
                ('day', models.CharField(choices=[('SAT', 'Saturday'), ('SUN', 'Sunday'), ('MON', 'Monday'), ('TUES', 'Tuesday'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'FRIDAY')], max_length=50)),
            ],
        ),
    ]
