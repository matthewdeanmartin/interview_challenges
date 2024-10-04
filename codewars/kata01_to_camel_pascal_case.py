def splitter(text):
    text = text.replace("-", "_")
    words = text.split("_")
    return list(word.strip("_") for word in words)


def to_camel_case(text):
    if not text:
        return ""
    words = splitter(text)
    result = []

    start_with_upper = text[0] == text[0].upper()

    for word in words:
        if len(word) == 0:
            continue
        elif len(word) == 1:
            new_word = word[0].upper()
            result.append(new_word)
        elif len(word) >= 2:
            new_word = word[0].upper() + word[1:]
            result.append(new_word)
        else:
            raise TypeError(f"What did I not consider {word}")
    almost_done = "".join(result)

    # TODO: extract to function
    if len(almost_done) == 0:
        almost_done = ""
    elif len(almost_done) == 1:
        if not start_with_upper:
            almost_done = almost_done[0].lower()
    elif len(almost_done) >= 2:
        if not start_with_upper:
            almost_done = almost_done[0].lower() + almost_done[1:]
    else:
        raise TypeError(f"What did I not consider {almost_done}")

    return almost_done

