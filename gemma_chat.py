import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = "Paste your API key here"


class Chat:
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    genai.configure(api_key=GOOGLE_API_KEY)


    def __init__(self):
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

    def chat(self):
        """
        Start a chat here
        :param txt:
        :return:
        """
        choice = True
        prompt_1 = ''
        response_1 = ''
        while choice == True:

            prompt_2 = input("You: ")
            chat_prompt = f"""
            <s>[INST] {prompt_1} [/INST]
            {response_1}
            </s>
            <s>[INST] {prompt_2} [/INST]
            """
            response_2 = self.model.generate_content(chat_prompt)
            prompt_1 = prompt_2
            response_1 = response_2.text
            print(f'Bot: {response_2.text}')
            # choice = True if input('1/0') == '1' else False

person = Chat()
person.chat()
