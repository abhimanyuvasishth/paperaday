from openai import OpenAI


def get_simplified_abstract(abstract):
    prompt = "Simplify this abstract into a paragraph 100 words or fewer for a high school level"
    prompt += f" {abstract}"
    messages = [
        {'role': 'user', 'content': prompt},
    ]

    response = OpenAI().chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200
    )

    return response.choices[0].message.content
