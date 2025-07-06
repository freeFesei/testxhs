from prompt_template import system_template_text, user_template_text
# from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu

# import os


def generate_xiaohongshu(theme, openai_api_key):

    # model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    model = ChatDeepSeek(model="deepseek-chat", api_key=openai_api_key,api_base='https://api.deepseek.com')
    output_parser = JsonOutputParser(pydantic_object=Xiaohongshu)

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])


    chain = prompt | model | output_parser

    print(output_parser.get_format_instructions())
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    print(type(result))

    print(result)
    print(result['titles'])
    return result

# print(generate_xiaohongshu("大模型", os.getenv("OPENAI_API_KEY")))
