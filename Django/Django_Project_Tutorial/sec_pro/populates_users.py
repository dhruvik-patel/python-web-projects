import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sec_pro.settings')

import django
django.setup()

from apptwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]

if __name__ == '__main__':
    print("POPULATING DATABASES")
    populate(20)
    print("COMPLETE")
