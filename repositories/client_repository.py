from sqlalchemy.orm import Session


class ClientRepository:
    def create_client(self, db: Session, entity):
        db.add(entity)
        db.commit()
