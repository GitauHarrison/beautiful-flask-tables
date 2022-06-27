from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    email = db.Column(db.String(120), index=True)
    phone = db.Column(db.String(64))
    address = db.Column(db.String(256))

    def __repr__(self):
        return 'User: {}'.format(self.username)

    def to_dict(self):
        return {
            'username': self.username,
            'age': self.age,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }
