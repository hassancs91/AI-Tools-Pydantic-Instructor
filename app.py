from pydantic import BaseModel
from typing import List
from helpers import structured_generator

#Replace With Your Output
class Titles(BaseModel):
    titles: List[str]

#Replace with your input
input = "Digital marketing"

#Replace with your prompt
prompt = f"generate 5 blog titles for a video about {input}" 

#Replace With Your Model
openai_model = "gpt-3.5-turbo"

result = structured_generator(openai_model,prompt,Titles)
print(result.titles)