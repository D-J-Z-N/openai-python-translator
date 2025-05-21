import tiktoken

def exceeds_token_limit(text: str, max_tokens: int = 200, model: str = "gpt-4") -> bool:
    
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base") 

    num_tokens = len(encoding.encode(text))

    return num_tokens > max_tokens
