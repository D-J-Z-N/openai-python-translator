import os
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from translator.is_too_long import is_too_long

load_dotenv()
console = Console()


def translate(text):

    if is_too_long(text):
        raise ValueError("The text is too long.")

    token = os.getenv("OPENAI_API_KEY")
    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1-nano"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful translator, that provides an accurate translation from English to Lithuanian.",
            },
            {"role": "user", "content": text}

        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    return response.choices[0].message.content
