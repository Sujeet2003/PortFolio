# Generated by Django 5.1.2 on 2024-10-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Base', '0003_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Programming', 'Programming'), ('Database', 'Database'), ('Aiml', 'Aiml'), ('Data_Visualization', 'Data_Visualization'), ('Others', 'Others'), ('Soft_Skills', 'Soft_Skills')], default='Others', max_length=100)),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
    ]
