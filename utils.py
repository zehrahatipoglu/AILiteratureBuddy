from openai import OpenAI
import arxiv
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_arxiv(query, max_results=5):
    search = arxiv.Search(query=query, max_results=max_results)
    return [(r.title, r.summary, r.entry_id) for r in search.results()]

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen bilimsel bir makale özetçisisin."},
            {"role": "user", "content": f"Lütfen bu metni 3 cümleyle özetle:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content


