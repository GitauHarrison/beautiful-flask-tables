import random
import sys
from app.models import Admin
from app import db, faker


def create_fake_users(n):
    """Generate fake users"""
    for i in range(n):
        admin = Admin(
            username=faker.user_name(),
            email=faker.email(),
            age=random.randint(18, 60),
            address=faker.address().replace('\n', ' '),
            phone=faker.phone_number()
        )
        db.session.add(admin)
    db.session.commit()
    print('Generated {} fake users to the database'.format(n))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of users you want to create as an argument')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]))
