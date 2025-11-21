import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_API_BASE_URL")
)

response = client.responses.create(   
  model="o3", 
  tools=[{"type": "web_search_preview"}], 
  input="Microsoft Ignite 2025 で発表された最新情報をまとめてください。"
)

print(response.output_text)
