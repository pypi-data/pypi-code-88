import unicodedata


def _is_control(char):
    """Checks whether `char` is a control character."""
    # These are technically control characters but we count them as whitespace
    # characters.
    if char == "\t" or char == "\n" or char == "\r":
        return False
    cat = unicodedata.category(char)
    if cat.startswith("C"):
        return True
    return False


def clean_text(text):
    """
    - NFC Normalization
    - Whitespace cleanup
      - strip()
      - double whitespace, \n, \r, \t -> simple whitespace (" ")
      - Unify all Zs to simple whitespace (" ")
    - Invalid character removal (Some control character)
    """
    text = unicodedata.normalize("NFC", text)

    text = " ".join(text.strip().split())

    output = []
    for char in text:
        if not _is_control(char):
            output.append(char)

    return "".join(output)
