import requests

def getBooks(number_of_books):
    data = requests.get(f'https://fakerapi.it/api/v1/books?_quantity={number_of_books}')
    books = data.json()['data'][0]
    print(books)

from faker import Faker

def getProfile():
    fake = Faker()
    return fake.profile()

from flask_api.models import Patient
from flask_api import db
import os
def seedData():
    for seed_num in range(10):
        data = getProfile()
        print(os.environ.get('DATABASE_URL'))
        print(data['name'],data['blood_group'])
        patient = Patient(
            data['name'],\
            data['sex'],\
            data['address'],\
            data['ssn'],\
            data['blood_group'],\
            data['mail'])

        db.session.add(patient)
        db.session.commit()        
seedData()