from gemini_client import get_response
from prompts import BASIC_PROMPT

def test_basic_response():
    response = get_response(BASIC_PROMPT)
    print(response)
    assert len(response) > 10