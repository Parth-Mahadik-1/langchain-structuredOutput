from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    temperature=0.7
)

model = ChatHuggingFace(llm = llm )

class person(BaseModel):

    name : str = Field(description="Name of the person")
    age : int = Field(gt = 18 ,description="Age of person")
    sal : int = Field(gt = 10000 ,description="salary of person")
    mode : str = Field(description="mode of currancy")


parser = PydanticOutputParser(pydantic_object=person)

template1 = PromptTemplate(
    template= "Give name, age and salary  and mode currancy of MD of {company} {country}\n {format_instruction}",
    input_variables= ['company','country'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template1.invoke(
    {
        "company":"relience of companies " , 
        "country":"india"
        })

result = model.invoke(prompt)

final_output = parser.parse(result.content)

print(final_output)


    
