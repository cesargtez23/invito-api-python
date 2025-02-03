from src.extensions import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, default='')
    description = db.Column(db.String, nullable=False, default='')
    user_id = db.Column(db.Integer, nullable=False)
    event_category_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    location_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    visibility = db.Column(db.Integer, nullable=False)
    is_trash = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'event_category_id': self.event_category_id,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'location_id': self.location_id,
            'status': self.status,
            'visibility': self.visibility,
            'is_trash': self.is_trash,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
