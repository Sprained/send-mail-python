from pydantic import BaseModel, Field

class CreateClientInternalBase(BaseModel):
    master_key: str = Field(
        ...,
        description="Chave de acesso unica para criar um novo usuario"
    )