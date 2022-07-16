from .db import db
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Statistic(db.Model):
    __tablename__ = 'statistics'

    id = db.Column(db.Integer, primary_key=True)
    won = db.Column(db.Integer, nullable=False)
    lost = db.Column(db.Integer, nullable=False)
    current_winning_streak = db.Column(db.Integer, nullable=False)
    longest_winning_streak = db.Column(db.Integer, nullable=False)
    longest_losing_streak = db.Column(db.Integer, nullable=False)
    total_games = db.Column(db.Integer, nullable=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'won': self.won,
            'lost': self.lost,
            'current_winning_streak': self.current_winning_streak,
            'longest_winning_streak': self.longest_winning_streak,
            'longest_losing_streak': self.longest_losing_streak,
            'total_games': self.total_games,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
