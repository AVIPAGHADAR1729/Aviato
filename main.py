import uvicorn
import granian
from app import app

if __name__ == "__main__":
    try:

        granian.Granian(target="app:app", address="127.0.0.1",
                        interface=granian.server.Interfaces.ASGI,
                        port=5000,
                        log_level=granian.server.LogLevels.debug,
                        websockets=False, respawn_failed_workers=True,
                        backlog=100000).serve()
    except Exception as e:
        print(f"Server exit with error: {e}")
