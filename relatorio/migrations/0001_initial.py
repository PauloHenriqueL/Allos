# Generated by Django 5.2 on 2025-04-16 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Terapeuta', '0002_rename_abordagem_terapeuta_abordagem_and_more'),
        ('decano', '0001_initial'),
        ('pacientes', '0002_remove_paciente_quantidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('sessao_1_realizado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_1_pago', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_2_realizado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_2_pago', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_3_realizado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_3_pago', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_4_realizado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('sessao_4_pago', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se aplica', 'Não se aplica')], default='Não', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Terapeuta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relatorio', to='Terapeuta.terapeuta')),
                ('decano', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relatorio', to='decano.decano')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relatorio', to='pacientes.paciente')),
            ],
            options={
                'ordering': ['Terapeuta'],
            },
        ),
    ]
