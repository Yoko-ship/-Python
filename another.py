import requests
import json
import openai
from bs4 import BeautifulSoup
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display,Markdown



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = "AIzaSyD2hNe7LapSNlyNyNiIVawvDQHBeOBvjks"


genai.configure(api_key=GOOGLE_API_KEY)



model = genai.GenerativeModel('models/gemini-pro')
condition = True
while condition:
  userInput = input("Введите то что вы хотите узнать: // q чтобы покинуть ")
  if userInput == "q":
    condition = False

  else:
    response = model.generate_content(userInput)

    with open('otvet.text','a',encoding="utf-8")as file:
      userChoice = input("Если хочешь добавить вариант напиши Вариант // если хочешь добавить  вопрос  внутри варианта напиши Вопрос: ")
      if userChoice == "Вариант":
        file.write("вариант №" + "\n")
      if userChoice == "Вопрос":
        file.write("-" * 50 + "\n")
      file.write(f'{response.text} \n')
      print("Файл был успешно записан")



