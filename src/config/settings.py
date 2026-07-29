from dotenv import load_dotenv
import os


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///pipeline.db")

RAW_DATA_PATH = os.getenv(
    "RAW_DATA_PATH",
    "data/raw/kpc_pipeline_sensor_data.csv"
)

PROCESSED_DATA_PATH = os.getenv(
    "PROCESSED_DATA_PATH",
    "data/processed/clean_pipeline_data.csv"
)