from gemini_client import get_response

def test_failure_handling():
    try:
        response = get_response(None)
        print(response)
    except Exception as e:
        print("Handled error:", e)