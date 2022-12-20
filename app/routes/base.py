from __future__ import annotations

from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def base_route():
    """
    Success Response for health check
    """
    return JSONResponse(content={
        "message": "Successful"
    }, status_code=200)


@router.get('/health')
async def perform_healthcheck():
    status_code = 200

    return JSONResponse(content={
        'healthcheck': 'Running',
    }, status_code=status_code)