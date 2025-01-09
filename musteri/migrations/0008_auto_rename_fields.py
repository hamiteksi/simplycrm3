from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('musteri', '0007_alter_yapilacak_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yapilacak',
            name='baslik',
        ),
        migrations.RemoveField(
            model_name='yapilacak',
            name='aciklama',
        ),
        migrations.AddField(
            model_name='yapilacak',
            name='yapilacak',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yapilacak',
            name='detay',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yapilacak',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, to='musteri.customer'),
        ),
    ] 