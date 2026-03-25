from gemini_client import get_response

def test_token_limit():
    long_input = "Explain GenAI. " * 500
    response = get_response(long_input, max_tokens=100)
    print(response)