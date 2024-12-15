import os
from typing import Any

from fastapi import FastAPI, APIRouter

from google.cloud import firestore
from pydantic.v1 import BaseSettings


def create_app():
    app = FastAPI(title=__name__)
    router = APIRouter(prefix="/api")
    app.config = EnvVars()
    app.firestore = firestore.Client()

    return app, router


class EnvVars(BaseSettings):

    def __init__(self, **values: Any):
        super().__init__(**values)
        self.app_config()

    @classmethod
    def app_config(cls):
        cls.SEND_GRID_API_KEY = os.environ.get("SEND_GRID_API_KEY")
