# Generated by Django 2.2.14 on 2020-08-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0017_update_constraintname_order_and_label'),
    ]

    def forward(apps, schema_editor):
        SlideSubmissionStatusName = apps.get_model('name', 'SlideSubmissionStatusName')
        slide_submission_status_names = [
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ]
        for order, (slug, desc) in enumerate(slide_submission_status_names):
            SlideSubmissionStatusName.objects.create(slug=slug, name=slug, desc=desc, used=True, order=order)


    def reverse(apps, schema_editor):
        pass

    operations = [
        migrations.CreateModel(
            name='SlideSubmissionStatusName',
            fields=[
                ('slug', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('used', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
                'abstract': False,
            },
        ),
        migrations.RunPython(forward, reverse),
    ]