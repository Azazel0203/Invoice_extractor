from dotenv import load_dotenv
from google.generativeai.generative_models import GenerativeModel
import os
from PIL import Image
import google.generativeai as genai
from src.prompt import input_prompt


def load_key() -> str:
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    return API_KEY


def gemini_init(model_type:str = 'gemini-pro-vision') -> GenerativeModel:
    key = load_key()
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_type)
    return model
    

def get_response(model: GenerativeModel, image:Image, user_prompt:str, input_prompt:str = input_prompt) -> str:
    response = model.generate_content([input_prompt, image, user_prompt])
    print(response)
    return response.candidates[0].content.parts[0].text.strip()
    



