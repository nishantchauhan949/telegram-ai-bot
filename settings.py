import logging
import os

from dotenv import load_dotenv

load_dotenv('.env')

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BARD_API_KEY = os.environ.get('BARD_API_KEY')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
