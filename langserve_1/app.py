from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPEAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Simple API server",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("Provide me an eassy about {topic}")
prompt1 = ChatPromptTemplate.from_template("Provide me a poem about {topic}")

add_routes(
    app,
    prompt | model,
    path = "/essay"
)

add_routes(
    app,
    prompt1 | model,
    path = "/poem"
)

if __name__  == "__main__":
    uvicorn.run(app,host="localhost",port=8000)