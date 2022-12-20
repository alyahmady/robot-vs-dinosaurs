import logging

import uvicorn
from app.errors import CustomException
from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.routes import base

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base.router)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define the logging filter for health check
class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        filter_result = super(EndpointFilter, self).filter(record=record)
        return bool(filter_result and (record.getMessage().find("/health") == -1))


# Add filter to the logger
logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.code, content={"status": False, "message": exc.message},
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content={"status": False, "message": exc.detail},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
