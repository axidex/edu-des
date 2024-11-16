import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    des_port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("DES_PORT", settings.des_port))
    uvicorn.run("src.app:app", host="0.0.0.0", port=port)
