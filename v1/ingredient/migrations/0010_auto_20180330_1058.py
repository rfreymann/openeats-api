# Generated by Django 2.0.1 on 2018-03-30 10:58

from django.db import migrations
from fractions import Fraction


def make_fraction(apps, schema_editor):
    # We can't import the Ingredient model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Ingredient = apps.get_model('ingredient', 'Ingredient')
    for i in Ingredient.objects.all():
        fraction = Fraction(i.quantity).limit_denominator(100)
        i.numerator = fraction.numerator
        i.denominator = fraction.denominator
        i.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0009_auto_20180330_1055'),
    ]

    operations = [
        migrations.RunPython(make_fraction),
    ]