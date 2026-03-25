from gemini_client import get_response

def test_empty_prompt():
    response = get_response("")
    print(response)

def test_ambiguous_prompt():
    response = get_response("Explain this")
    print(response)