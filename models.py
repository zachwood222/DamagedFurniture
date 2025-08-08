from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text
from datetime import datetime
import enum

Base = declarative_base()

class Status(enum.Enum):
    NEW = 'NEW'
    RESOLVED = 'RESOLVED'
    CREDIT_RECEIVED = 'CREDIT_RECEIVED'

class EmailItem(Base):
    __tablename__ = 'email_items'
    id = Column(Integer, primary_key=True)
    gmail_message_id = Column(String(128), unique=True, index=True)
    thread_id = Column(String(128))
    account_email = Column(String(255))

    sender = Column(String(255))
    subject = Column(String(1000))
    date = Column(String(128))  # RFC822 string
    snippet = Column(Text)

    status = Column(Enum(Status), default=Status.NEW, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    photos = relationship('Photo', back_populates='email_item', cascade='all, delete-orphan')

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    email_item_id = Column(Integer, ForeignKey('email_items.id', ondelete='CASCADE'))

    filename = Column(String(512))
    mime_type = Column(String(255))
    size = Column(String(64))

    drive_file_id = Column(String(128))
    web_view_link = Column(String(1024))
    web_content_link = Column(String(1024))

    email_item = relationship('EmailItem', back_populates='photos')
