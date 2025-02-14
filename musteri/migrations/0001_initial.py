# Generated by Django 4.2.7 on 2025-01-05 15:52

from django.db import migrations, models
import django.db.models.deletion
import musteri.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PHONE', 'Telefon'), ('EMAIL', 'E-posta'), ('SMS', 'SMS'), ('WHATSAPP', 'WhatsApp'), ('MEETING', 'Görüşme'), ('OTHER', 'Diğer')], max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'İletişim Kaydı',
                'verbose_name_plural': 'İletişim Kayıtları',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fee_first_year', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee_next_year', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('customer_notes', models.TextField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('income', models.CharField(blank=True, max_length=100, null=True)),
                ('income_source', models.CharField(blank=True, max_length=100, null=True)),
                ('insurance_type', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('appointment_place', models.CharField(blank=True, max_length=100, null=True)),
                ('identity_number', models.CharField(blank=True, max_length=20, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=20, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=20, null=True)),
                ('issuing_authority', models.CharField(blank=True, max_length=100, null=True)),
                ('passport_date', models.CharField(blank=True, max_length=100, null=True)),
                ('passport_info', models.TextField(blank=True, null=True)),
                ('passport_type', models.CharField(blank=True, max_length=100, null=True)),
                ('application_type', models.CharField(blank=True, max_length=50, null=True)),
                ('residence_type', models.CharField(blank=True, max_length=50, null=True)),
                ('residence_permit_start_date', models.DateField(blank=True, null=True)),
                ('residence_permit_end_date', models.DateField(blank=True, null=True)),
                ('service_type', models.CharField(blank=True, max_length=50, null=True)),
                ('ptt_code', models.CharField(blank=True, max_length=100, null=True)),
                ('application_number', models.CharField(blank=True, max_length=100, null=True)),
                ('application_date', models.DateField(blank=True, default=None, help_text='Müşterinin başvuru tarihi', null=True, verbose_name='Başvuru Tarihi')),
                ('payment_made', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('ACTIVE', 'Aktif'), ('INACTIVE', 'Pasif'), ('PENDING', 'Beklemede'), ('COMPLETED', 'Tamamlandı')], default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('communication_history', models.ManyToManyField(blank=True, related_name='related_customers', to='musteri.communication')),
            ],
            options={
                'verbose_name': 'Müşteri',
                'verbose_name_plural': 'Müşteriler',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'), (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110'), (111, '111'), (112, '112'), (113, '113'), (114, '114'), (115, '115'), (116, '116'), (117, '117'), (118, '118'), (119, '119'), (120, '120')])),
                ('country', models.CharField(choices=[('TR', 'Turkey'), ('US', 'USA'), ('UK', 'United Kingdom')], max_length=2)),
                ('contract_fee', models.BooleanField(default=False)),
                ('population_fee', models.BooleanField(default=False)),
                ('card_fee', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceAgeBracket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=200)),
                ('fee_first', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee_second', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Yapilacak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yapilacak', models.CharField(max_length=200)),
                ('detay', models.TextField(blank=True, null=True)),
                ('son_tarih', models.DateTimeField()),
                ('tamamlandi', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musteri.customer')),
            ],
            options={
                'verbose_name': 'Yapılacak',
                'verbose_name_plural': 'Yapılacaklar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='musteri.customer')),
            ],
            options={
                'verbose_name': 'Ödeme',
                'verbose_name_plural': 'Ödemeler',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='musteri.customer')),
            ],
            options={
                'verbose_name': 'Not',
                'verbose_name_plural': 'Notlar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='musteri.customer')),
            ],
            options={
                'verbose_name': 'Gider',
                'verbose_name_plural': 'Giderler',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='CustomerFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to=musteri.models.get_upload_to)),
                ('file_description', models.CharField(blank=True, max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='musteri.customer')),
            ],
        ),
        migrations.AddField(
            model_name='communication',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communications', to='musteri.customer'),
        ),
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar_events', to='musteri.customer')),
            ],
            options={
                'verbose_name': 'Takvim Etkinliği',
                'verbose_name_plural': 'Takvim Etkinlikleri',
                'ordering': ['start_time'],
            },
        ),
    ]
