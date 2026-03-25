import time
from gemini_client import get_response

def test_latency():
    start = time.time()
    response = get_response("Explain GenAI latency in production")
    end = time.time()

    latency = end - start
    print("Latency:", latency)

    assert latency < 10