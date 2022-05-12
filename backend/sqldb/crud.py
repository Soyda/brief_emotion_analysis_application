from sqlalchemy.orm import Session
from . import models, schemas
import csv


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password #+ "notreallyhashed"
    db_user = models.User(is_admin=user.is_admin, username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()


def create_user_note(db: Session, note: schemas.NoteCreate, user_id: int):
    db_note = models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note



# add some data
# def fill_db(db):
#     with open("dummy_data/dummy_data.csv", "r") as f:
#         csv_reader = csv.DictReader(f)

#     for row in csv_reader:
#         db_record = Note(
#             user= row["username"]
#             date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
#             note_content=row["note"],
#             sentiment=row["sentiment"],
#         )
#         db.add(db_record)

#     db.commit()

#     db.close()