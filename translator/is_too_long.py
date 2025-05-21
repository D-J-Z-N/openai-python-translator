import tiktoken

def is_too_long(text, max_tokens=200, model="gpt-4"):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base") 

    num_tokens = len(encoding.encode(text))
    return num_tokens > max_tokens
