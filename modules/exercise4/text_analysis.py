from exercise3.string_ops import count_vowels

def analyze_text(s:str) -> dict[str, int]:
    return {
        "length": len(s),
        "vowels": count_vowels(s)
    }


