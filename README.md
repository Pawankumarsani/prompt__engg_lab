# Prompt Engineering Lab

A small lab for comparing different prompt engineering patterns (zero-shot, few-shot, chain-of-thought, role prompting, and system prompting) on a sentiment classification task, using the Groq API (Llama 3.3 70B).

## Project Structure

```
prompt_engg_lab/
├── prompts.py      # All prompt pattern templates
├── evaluator.py     # Batch-runs every pattern against a fixed set of test texts
├── playground.py    # Interactive CLI to try one pattern at a time on your own text
└── .env             # API key (not included — you create this)
```

## Prompt Patterns

Defined in `prompts.py`:

| Pattern | Description |
|---|---|
| **Zero-Shot** | Directly asks the model to classify sentiment with no examples. |
| **Few-Shot** | Provides 3 labeled examples before asking the model to classify. |
| **Chain-of-Thought** | Asks the model to reason step-by-step before classifying. |
| **Role Prompt** | Frames the model as an "expert sentiment analyst" before classifying. |
| **System Prompt** | Uses a system message with strict output rules (one-word answer only). |

## Requirements

- Python 3.9+
- A [Groq API key](https://console.groq.com/keys)

## Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for environment management.

1. **Open a terminal in the project folder.**

2. **Create the virtual environment and install dependencies:**
   ```bash
   uv venv
   uv add groq python-dotenv
   ```

3. **Create a `.env` file** in the project root with your Groq API key:
   ```
   prompt_engg=your_groq_api_key_here
   ```

## Usage

### Evaluator — batch comparison

Runs all 4 non-system patterns (Zero-Shot, Few-Shot, Chain-of-Thought, Role Prompt) against 3 fixed test texts and prints the results side by side:

```bash
uv run evaluator.py
```

Example output:
```
Text: What a lovely weather
----------------------------------------
Zero_Shot:Positive | Tokens: 42
Few_shot:Positive | Tokens: 45
Chain_of _thought:Positive | Tokens: 58
Role_Prompt:Positive | Tokens: 51
```

### Playground — interactive single-pattern testing

Lets you pick one pattern at a time and test it on any text you enter:

```bash
uv run playground.py
```

```
==== Prompt Engineering Playground ====
Patterns: 1-Zero_shot 2-Few_shot 3-Chain_of_thought 4-Role 5- System

Choose patterns (1-5) or quit: 1
Enter text analysis: This is amazing!

Pattern: Zero_Shot
Result: Positive
Tokens used: 40
```

Type `quit` to exit.

## Configuration

- **Model:** `llama-3.3-70b-versatile` (edit the `model` parameter in `evaluator.py` / `playground.py` to change it)
- **Max tokens:** capped at 50 per response — enough for a short label/explanation, adjust if you extend the prompts
- **Test texts:** edit the `test_texts` list in `evaluator.py` to try different inputs

## Known Issues / Possible Improvements

- `evaluator.py` doesn't include the System Prompt pattern in its comparison loop (only `playground.py` uses it) — could be added for full parity.
- No error handling around the Groq API calls (rate limits, auth errors, connection issues) — worth adding, especially for batch runs in `evaluator.py`.
- A few typos in `prompts.py` ("Posivite", "terible", "explaination") — harmless since they're just prompt text, but worth fixing for clarity.
- Token counts and outputs aren't logged to a file — results only print to console and are lost after the run.
- `test_texts` and `patterns` dictionaries are hardcoded; could be moved to a config file for easier experimentation.

## License

Add a license of your choice (MIT is a common default for personal projects).