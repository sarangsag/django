# Generated by Django 3.0 on 2022-06-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=100)),
                ('pcompany', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to='')),
                ('pram', models.CharField(max_length=100)),
                ('prom', models.CharField(max_length=100)),
                ('pcolor', models.CharField(max_length=100)),
                ('pprice', models.IntegerField()),
                ('pitems', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('dmail', models.EmailField(max_length=50)),
                ('pprice', models.CharField(max_length=50)),
                ('pcolor', models.CharField(max_length=50)),
                ('pram', models.CharField(max_length=50)),
                ('prom', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('dt', models.DateTimeField()),
                ('lmark', models.CharField(max_length=50)),
                ('dtype', models.CharField(max_length=20)),
                ('file', models.ImageField(upload_to='')),
                ('pid', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='feedbackmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('sub', models.CharField(max_length=100)),
                ('mes', models.CharField(max_length=100)),
                ('dt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='usmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('uage', models.IntegerField()),
                ('uphone', models.CharField(max_length=50)),
                ('umail', models.EmailField(max_length=50)),
                ('upsw', models.CharField(max_length=8)),
            ],
        ),
    ]
