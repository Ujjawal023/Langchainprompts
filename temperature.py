from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

#chat model 
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)

result = model.invoke("write a 5 line poem on cricket")
print(result.content)