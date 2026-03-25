# 🧪 LLM Testing Pro (Gemini API Test Suite)

A comprehensive, automated testing suite built with **`pytest`** to strictly evaluate, validate, and benchmark responses given by the **Google Gemini API**. It models the behavior of large language models under various constraints like token limits, prompt complexities, edge cases, and connection latencies.

## ✨ Features
- **Validation Testing**: Verifies that standard prompts return semantically correct and properly formatted responses.
- **Latency Benchmarking**: Includes metrics tests to calculate and validate the latency overhead for API calls.
- **Token Constraints**: Actively tests the payload configuration boundaries (e.g., ensuring `max_output_tokens` behavior executes perfectly).
- **Failure & Edge Case Handling**: Validates system responses against extreme or unconventional prompts, as well as gracefully handling simulated failures.
- **Modular Architecture**: Separate configuration layers (`config.py`), prompt registries (`prompts.py`), and a dedicated AI client handler (`gemini_client.py`).

## 📁 File Structure

```
LLM_Testing_Pro/
│
├── .env                        # Private environment variables (API keys)
├── config.py                   # Centralizes execution variables like model names
├── gemini_client.py            # Primary handler constructing google-genai client
├── prompts.py                  # Static storage for benchmarking prompts
├── requirements.txt            # Required python modules
│
├── test_basic_response.py      # Assertions validating normal text returns
├── test_edge_cases.py          # Testing bizarre inputs or boundary conditions
├── test_failure_handling.py    # Assertations for exception handling and errors
├── test_latency.py             # Metrics testing API response speeds
└── test_token_limit.py         # Testing generation configurations (max_tokens)
```

## 🛠️ Prerequisites

Using this suite requires Python 3.9+ along with an active Google Gemini API Key.

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Core Dependencies:* `google-genai`, `python-dotenv`, `pytest`

2. **Configure Environment**
   Create a `.env` file at the root of the project to feed your API key:
   ```ini
   GEMINI_API_KEY="your-google-gemini-api-key"
   ```

## ⚙️ Running the Test Suite

Since the testing harness relies natively on `pytest`, you can easily execute all available tests to benchmark your API setup using a single command:

```bash
# Run all tests sequentially
pytest

# To view test output and latency prints explicitly:
pytest -s -v
```

### 🧠 Testing Focus Areas

- `BASIC_PROMPT`: Simple requests to check model uptime.
- `SHORT_PROMPT`: Instructs brevity to test if the model adheres precisely to formatting logic.
- `LONG_PROMPT`: Extensive generation for latency tracking and token saturation checks.
