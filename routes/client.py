from fastapi import APIRouter, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel

from interface.client_interface import CreateClientInternalBase
from services.client_service import ClientService
from utils.database import get_db

router = APIRouter(prefix="/client")

client_service = ClientService()


@router.post(
    "/internal",
    response_class=JSONResponse,
    summary="Criação de um novo usuario",
    status_code=201,
    responses={
        201: {
            "content": {
                "application/json": {
                    "examples": {"success": {"value": {"access_key": "teste"}}}
                }
            }
        },
        403: {
            "content": {
                "application/json": {
                    "examples": {
                        "invalid master_key": {
                            "value": {"detail": "Invalid key"}
                        }
                    }
                }
            }
        },
    },
)
async def create_client_internal(
    req: Request, data: CreateClientInternalBase, db: Session = Depends(get_db)
):
    result = client_service.create_client_internal(db, data.master_key)
    return JSONResponse(jsonable_encoder({"access_key": result}), 201)


# @router.patch()