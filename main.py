from dotenv import load_dotenv
import os  
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_key=os.getenv("Gemini_Api_Key")

system_prompt="""You are Nova, a friendly, witty, and intelligent AI assistant.  
You can answer any question the user asks — from serious topics to silly curiosities — 
with clarity, confidence, and a touch of humor.Keep your tone light, engaging, and positive.  
If the topic allows, sprinkle in a clever joke or playful remark, but never be rude or sarcastic.  
Your goal is to make the user smile while giving genuinely helpful and accurate answers.
ANswer in 2-4 lines.
"""

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)


history=[]

while True:
    user_input=input("You: ")
    if user_input=="exit":
        break
    history.append({"role":"user","content":user_input})
    response=llm.invoke([{"role":"system","content":"system_prompt"}]+history)
    print(f"Nova: {response.content}")
    history.append({"role":"user","content":response.content})