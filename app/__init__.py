from app.manage import create_app

# Create App
app, router = create_app()
from .apis import *

# Include router
app.include_router(router)
