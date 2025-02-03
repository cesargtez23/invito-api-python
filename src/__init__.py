from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models import Event
from src.extensions import db
from datetime import datetime

def create_app():
    # create and configure the app
    app = Flask(__name__)
       
    app.config.from_mapping(
            SECRET_KEY="dev",
            SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres.doazgwtfsnmxagvjierm:YDBnxhTVTYMMRHWu@aws-0-us-west-1.pooler.supabase.com:5432/postgres",
            DEBUG=False                     
        )
    
    db.init_app(app)

    # Create tables (for a production environment, you'd use migrations)
    with app.app_context():
        db.create_all()  

    #Routes

    @app.route('/events', methods=['GET'])
    def get_events():
        events = Event.query.all()
        return jsonify([event.serialize() for event in events]), 200
    
    @app.route('/events', methods=['POST'])
    def create_event():
        data = request.get_json()
        new_event = Event(
            title=data.get('title', ''),
            description=data.get('description', ''),
            user_id=data['user_id'],
            event_category_id=data['event_category_id'],
            start_time=datetime.fromisoformat(data['start_time']),
            end_time=datetime.fromisoformat(data['end_time']),
            location_id=data['location_id'],
            status=data['status'],
            visibility=data['visibility'],
            is_trash=data.get('is_trash', False),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.serialize()), 201

    @app.route('/events/<int:event_id>', methods=['DELETE'])
    def delete_event(event_id):
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully'}), 200
  
    return app

  
    