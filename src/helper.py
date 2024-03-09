from dotenv import load_dotenv
from google.generativeai.generative_models import GenerativeModel
import os
from PIL import Image
import google.generativeai as genai
from src.prompt import input_prompt


def load_key() -> str:
    """
    The function `load_key` loads a Google API key from environment variables.
    :return: The function `load_key()` is returning the Google API key stored in the environment
    variable "GOOGLE_API_KEY".
    """
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    return API_KEY


def gemini_init(model_type:str = 'gemini-pro-vision') -> GenerativeModel:
    """
    The function `gemini_init` initializes a GenerativeModel object using a specified model type in the
    Gem AI platform.
    
    :param model_type: The `model_type` parameter in the `gemini_init` function is a string parameter
    that specifies the type of GenerativeModel to be initialized. In this case, the default value for
    `model_type` is set to 'gemini-pro-vision', defaults to gemini-pro-vision
    :type model_type: str (optional)
    :return: A GenerativeModel object is being returned.
    """
    key = load_key()
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_type)
    return model
    

def get_response(model: GenerativeModel, image:Image, user_prompt:str, input_prompt:str = input_prompt) -> str:
    """
    The function `get_response` takes a generative model, an image, a user prompt, and an optional input
    prompt, generates content based on the prompts, and returns the generated response as a string.
    
    :param model: The `model` parameter is of type `GenerativeModel`, which is likely a machine learning
    model used for generating content based on input prompts
    :type model: GenerativeModel
    :param image: The `image` parameter is an image input that is being passed to the `get_response`
    function. It is likely used as part of the input to the `GenerativeModel` for generating a response
    based on the provided `user_prompt` and `input_prompt`
    :type image: Image
    :param user_prompt: The `user_prompt` parameter is a string that represents the prompt or input
    provided by the user. It is used as part of the input to the generative model to generate a response
    :type user_prompt: str
    :param input_prompt: The `input_prompt` parameter is a string that represents the prompt given to
    the model to generate a response. It is used as part of the input to the `generate_content` method
    of the `GenerativeModel` along with the `image` and `user_prompt` to generate a response
    :type input_prompt: str
    :return: The function `get_response` returns the generated response as a string.
    """
    response = model.generate_content([input_prompt, image, user_prompt])
    print(response)
    return response.candidates[0].content.parts[0].text.strip()
    



