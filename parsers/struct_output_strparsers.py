from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    temperature=0.7
)

model = ChatHuggingFace(llm = llm )

template1 = PromptTemplate(
    template="Write deatiled about the {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write 5 line summary on   the {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chains = template1 | model | parser | template2 | model | parser

result = chains.invoke({"topic":"Google"})

print(result)