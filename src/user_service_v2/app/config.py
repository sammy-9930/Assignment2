import os 
import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)

logger = logging.getLogger("user_service_v2")

class Config:
    MONGO_URI=os.getenv("MONGO_URI")
    USER_DB=os.getenv("USER_DB")
    RABBITMQ_URI = os.getenv("RABBITMQ_URI")
    RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
    RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
    RABBITMQ_QUEUE_NAME = os.getenv("RABBITMQ_QUEUE_NAME")