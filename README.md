# Vibesort

AI-powered array sorting and value comparison using GPT.

## Usage

Install the package:
```bash
pip install vibesort
```

Set your OpenAI API key as an environment variable.
```bash
export OPENAI_API_KEY=your_key_here
```

### Sorting Arrays

```python
from vibesort import vibesort

result = vibesort([5, 2, 8, 1, 9])
print(result)  # [1, 2, 5, 8, 9]
```

### Comparing Values with AI

The `vibeequals` function uses AI to determine if two values are semantically or conceptually equal, even if they differ in format or representation:

```python
from vibesort import vibeequals

# Different formats, same meaning
print(vibeequals("42", 42))        # True
print(vibeequals("Hello", "hello")) # True  
print(vibeequals("yes", "true"))   # True

# Truly different values
print(vibeequals("hello", "goodbye")) # False
print(vibeequals(42, 7))              # False
```

## Test

```bash
pytest tests/
```

## Dependencies

- openai
- pydantic  
- typing-extensions

⚠️ Requires OpenAI API key. Experimental project - not for production use.
