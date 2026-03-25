# # import google.generativeai as genai
# from google import genai
# from config import GEMINI_API_KEY, MODEL_NAME

# genai.Client(api_key=GEMINI_API_KEY)

# model = genai.GenerativeModel(MODEL_NAME)

# def get_response(prompt, max_tokens=200):
#     response = model.generate_content(
#         prompt,
#         generation_config={
#             "max_output_tokens": max_tokens,
#             "temperature": 0.3
#         }
#     )
#     return response.text


from google import genai
from config import GEMINI_API_KEY, MODEL_NAME

# create client
client = genai.Client(api_key=GEMINI_API_KEY)

def get_response(prompt: str, max_tokens: int = 200) -> str:
    response = client.models.generate_content(
        model= MODEL_NAME,
        contents = prompt,
        config={
            "max_output_tokens": max_tokens,
            "temperature": 0.3
        }
    )
    return response.text