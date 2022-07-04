"""
Factory method to generate dummy data for models testing

Example to write dummy data to ddbb using django shell
# python manage.py shell
from analyses.models import Analyses
a = Analyses(description="RM sin contraste", modality="MRT T1w", customer="Qubiotech", status="Finished")
a.save()
Analyses.objects.all()
# >>> from analyses.models import Analyses
# >>> Analyses.objects.all()
"""

from faker import Faker
fake = Faker()

# To avoid error: django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet
import django
django.setup()

import factory
import factory.fuzzy

import sys
import os.path as op
from authenticate.models import User

class UserFactory(factory.Factory):

    class Meta: 
        model = User
    
    email = factory.Faker("email")
    username = factory.Faker("username")
    first_name = factory.Faker("name")
    last_name = factory.Faker("name")
    phone = factory.Faker("phone_number")

if __name__ == "__main__":
    analyses = AnalysesFactory.create_batch(10)
    for i, analysis in enumerate(analyses):
        print(f'ID: {i}: \n => Decription: {analysis.description}, Modality: {analysis.modality}, Status: {analysis.status}, Customer: {analysis.customer}')