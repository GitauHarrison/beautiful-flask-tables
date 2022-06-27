from app import db
from app.models import User
from faker import Faker
from random import randint
import sys


def create_fake_users(total):
    fake = Faker()
    for i in range(total):
        user = User(
            username=fake.user_name(),
            age=randint(18, 100),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
            )
        db.session.add(user)
    db.session.commit()
    print(f'Created {total} fake users and added them to the database')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Please provide the number of users as an argument')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]))
