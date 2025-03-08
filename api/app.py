from fastapi import FastAPI
import uvicorn
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version = '1.0',
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 150 words")

add_routes(
    app,
    prompt|model,
    path='/essay'
)


if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)
