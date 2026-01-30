def reverse_string(s: str) -> str:
    reverse: str = ""
    for i in range(len(s) - 1, -1, -1):
        reverse += s[i]

    return reverse


def count_vowels(s: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}

    return len([c for c in s if c.lower() in vowels])


if __name__ == "__main__":
    print(reverse_string("!esicrexE looC"))
