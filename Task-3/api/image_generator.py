import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = (
"https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
)

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_image(prompt):

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    return response.content
