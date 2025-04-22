from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    # Create the columns
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Foreign key to User

    # Relationship to user (many tasks -> 1 user)
    owner = relationship("User", back_populates="tasks")

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())