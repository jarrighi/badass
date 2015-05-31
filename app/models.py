from app import db

class Skill(db.Model):
    __tablename__ = "skills"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    level = db.Column(db.Integer)

    def __init__(self, title, level):
        self.title = title
        self.level = level

    def __repr__(self):
        return '<level {}: {}>'.format(self.level, self.title)