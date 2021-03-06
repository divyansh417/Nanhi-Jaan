# Generated by Django 2.1.2 on 2019-02-16 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attention', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('generalInfo', models.CharField(max_length=2000)),
                ('status', models.CharField(max_length=5)),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodInfo', models.CharField(max_length=500)),
                ('diseaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapi.DiseaseInfo')),
            ],
        ),
        migrations.CreateModel(
            name='MentalExerciseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MentalInfo', models.CharField(max_length=500)),
                ('diseaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapi.DiseaseInfo')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExerciseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physicalInfo', models.CharField(max_length=500)),
                ('diseaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapi.DiseaseInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Prevention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prevention', models.CharField(max_length=500)),
                ('diseaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapi.DiseaseInfo')),
            ],
        ),
        migrations.CreateModel(
            name='SymptomInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptomInfo', models.CharField(max_length=500)),
                ('diseaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapi.DiseaseInfo')),
            ],
        ),
        migrations.AddField(
            model_name='attention',
            name='diseaseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sihapi.DiseaseInfo'),
        ),
    ]
