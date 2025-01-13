import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st
from dotenv import load_dotenv

from langchain.memory import ConversationBufferMemory

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.title("Celebrity Search Application")
input_text  = st.text_input("search for a celebrity you want to know more about")

llm = OpenAI(temperature=0.8)


prompt1 = PromptTemplate(
    input_variable=['name'],
    template="Tell me about celebrity {name}"
)
chain = LLMChain(llm=llm,prompt=prompt1,verbose=True,output_key = 'person')

prompt2 = PromptTemplate(
    input_variable=['person'],
    template="when was {person} born?"
) 
chain2 = LLMChain(llm=llm,prompt=prompt2,verbose=True,output_key = 'dob')

prompt3 = PromptTemplate(
    input_variable=['dob'],
    template="meantion 5 major events happend around {dob} in the world?"
) 
chain3 = LLMChain(llm=llm,prompt=prompt3,verbose=True,output_key = 'events')

parentChain = SequentialChain(chains = [chain,chain2,chain3],input_variables = ['name'],output_variables=['person','dob','events'],verbose=True)

if input_text:
    st.write(parentChain({'name':input_text}))
