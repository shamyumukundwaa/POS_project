from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.users import User


class UserRepository:
    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.user_id == user_id).first()

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()

    def create(
        self,
        db: Session,
        username: str,
        password: str,
        email: Optional[str] = None,
    ) -> User:
        user = User(
            username=username,
            password=password,
            email=email,
            is_active=True,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


user_repo = UserRepository()


def get_user_by_username(db: Session, username: str):
    return user_repo.get_by_username(db, username)


def create_user(
    db: Session, username: str, password: str, email: Optional[str] = None
):
    return user_repo.create(
        db, username=username, password=password, email=email
    )
