# Generated by Django 4.1.5 on 2023-05-12 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transact', '0003_remove_transactions_prenom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(default='', max_length=150, null=True)),
                ('nom', models.CharField(default='', max_length=150, null=True)),
                ('adresse', models.CharField(default='', max_length=150, null=True)),
                ('somme', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='nom',
        ),
        migrations.AddField(
            model_name='transactions',
            name='client',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='transact.client'),
        ),
    ]