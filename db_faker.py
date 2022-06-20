"""
Module to generate dummy data to test db
Reference: https://www.educative.io/courses/django-admin-web-developers/RLPEYWRpDPV
"""

import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.settings")

import django 
django.setup() 

from faker import factory, Faker 
from model_bakery.recipe import Recipe,foreign_key 

# Load models
# from sample_app.models import * 
from tasks.models import Task

fake = Faker() 

nsmaple = 10
def add_recipie():
    for k in range(nsample):
        author=Recipe(Author,
                    name=fake.name(),
                    createdDate=fake.future_datetime(end_date="+30d", tzinfo=None),
                    updatedDate=fake.future_datetime(end_date="+30d", tzinfo=None),)
    
        question=Recipe(Question, 
                    question_text=fake.sentence(nb_words=6,variable_nb_words=True),
                    pub_date=fake.future_datetime(end_date="+30d",tzinfo=None),
                    refAuthor=foreign_key(author),
                    createdDate=fake.future_datetime(end_date="+30d",tzinfo=None),
                    updatedDate=fake.future_datetime(end_date="+30d",tzinfo=None),)
        
        choice = Recipe(Choice, 
                    question=foreign_key(question), 
                    choice_text = fake.sentence(nb_words=1, variable_nb_words=True), 
                    createdDate=fake.future_datetime(end_date="+30d", tzinfo=None),  
                    updatedDate=fake.future_datetime(end_date="+30d", tzinfo=None), ) 
        choice.make()

def add_task():
    for k in range(nsample):
    task=Recipe(Author,
                title=fake.name(),
                description=fake.name())

    task = Task(title="Coding in Python",description="Building a REST API using django")
