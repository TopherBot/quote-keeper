import builtins
import sys
from importlib import reload

# Ensure the module can be imported fresh for each test run
def test_random_quote_returns_string():
    from src.quote_keeper import random_quote
    result = random_quote()
    assert isinstance(result, str)
    assert len(result) > 0

# Mock random.choice to guarantee deterministic output
def test_random_quote_with_mock(monkeypatch):
    from src.quote_keeper import random_quote, _QUOTES
    def fake_choice(seq):
        # Always return the first element
        return seq[0]
    monkeypatch.setattr('random.choice', fake_choice)
    assert random_quote() == _QUOTES[0]
