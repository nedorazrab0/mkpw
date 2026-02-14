# SPDX-License-Identifier: 0BSD

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from secrets import choice, SystemRandom
from get_wordlist import get_wordlist

def make_password(
    length: int,
    passphrase: bool,
    no_punctuation: bool,
    custom_chars: str
) -> str:
    if passphrase:
        wordlist = get_wordlist()
        password = ".".join(choice(wordlist) for _ in range(length))
    else:
        charsets = (
            "" if no_punctuation else punctuation,
            custom_chars if custom_chars else "",
            ascii_lowercase, ascii_uppercase, digits
        )
        required_chars = tuple(choice(charset) for charset in charsets
                               if charset)
        extra_length = length - sum(1 if charset else 0 for charset in charsets)
        charset = "".join(charsets)
        random_chars = tuple(choice(charset) for _ in range(extra_length))
        password = list(required_chars + random_chars)
        SystemRandom().shuffle(password)
        password = "".join(password)
    return password
