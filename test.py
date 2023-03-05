import openai

openai.api_key = "XX"

def translate_text(text):
    try:
        completion = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=f"Translate the following text to traditional chinese: {text}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        translated_text = completion.choices[0].text.strip()
        return translated_text
    except Exception as e:
        print(f"Error: {e}")
        return text

text = "Hello, how are you doing today?"
translated_text = translate_text(text)
print(f"Original text: {text}")
print(f"Translated text: {translated_text}")
