import random

_QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you’re busy making other plans. – John Lennon",
    "The purpose of our lives is to be happy. – Dalai Lama",
    "Get busy living or get busy dying. – Stephen King",
    "You have within you right now, everything you need to deal with whatever the world throws at you. – Brian Tracy",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
]

def random_quote() -> str:
    """Return a random inspirational quote."""
    return random.choice(_QUOTES)

if __name__ == "__main__":
    print(random_quote())
