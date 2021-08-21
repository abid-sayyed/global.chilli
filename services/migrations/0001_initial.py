# Generated by Django 3.2.6 on 2021-08-20 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_of_food', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], max_length=100)),
                ('portion_size', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], max_length=100)),
                ('ease_of_ordering', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], max_length=100)),
                ('overall_value', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], max_length=100)),
                ('suggestions', models.TextField(max_length=150)),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
