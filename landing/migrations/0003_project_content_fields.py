from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_activity_event_image_mediamention_image_partner_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_label',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='project',
            name='goal',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AddField(
            model_name='project',
            name='partners',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='participants',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='outcome',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='website_text',
            field=models.TextField(blank=True),
        ),
    ]