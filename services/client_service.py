import uuid
import os

from sqlalchemy.orm import Session
from fastapi import HTTPException

from repositories.client_repository import ClientRepository
from models import Client


class ClientService:
    def __init__(self):
        self.client_respository = ClientRepository()

    def create_client_internal(self, db: Session, master_key):
        if master_key != os.getenv("INTERNAL_KEY"):
            raise HTTPException(status_code=403, detail="Invalid key")

        access_key = uuid.uuid4()
        client = Client(access_key=access_key)
        self.client_respository.create_client(db, client)

        return access_key
