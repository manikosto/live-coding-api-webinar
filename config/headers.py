import os
from dotenv import load_dotenv

load_dotenv()

class Headers:

    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    }
