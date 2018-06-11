import random
from datetime import timedelta

from django.utils import timezone

from app1.models import Student

names = ['alice', 'bob', 'charlie', 'david', 'fiona', 'gabriel']
genders = [0, 1, 1, 1, 0, 1]
for name, gender in zip(names, genders):
    age = random.randint(18, 60)
    dt = timezone.now() - timedelta(days=random.randint(10, 45))
    Student.objects.create(name=name, gender=gender, age=age, time=dt)
