from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    temperature=0.7

)

model = ChatHuggingFace(llm = llm)

tamplate1 = PromptTemplate(
    template="explain in deatiled about the {topic} ",
    input_variables=['topic']

)

tamplate2 = PromptTemplate(
    template=  "give 5 line summary of {text}",
    input_variables=["text"]
)

prompt1  = tamplate1.invoke({"topic":"star sun"})

result1 = model.invoke(prompt1)

prompt2 = tamplate2.invoke({"text":result1.content})

result2 = model.invoke(prompt2)

print(result2.content)
