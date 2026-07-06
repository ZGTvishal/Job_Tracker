from pydantic_settings import BaseSettings, SettingsConfigDict
import os



class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = '.env')



    database_url: str 
    google_client_id: str
    google_client_secret: str 
    environment: str = "dev"
    debug: bool = False


settings = Settings()

