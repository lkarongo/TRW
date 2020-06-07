from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    notices = db.relationship("Notice", backref="address", lazy=True)

    def add_notice(self, notice):
        n = Notice(notice=notice, address_id=self.id)
        db.session.add(n)
        db.session.commit()


class Notice(db.Model):
    __tablename__ = "notices"
    id = db.Column(db.Integer, primary_key=True)
    notice = db.Column(db.String, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)