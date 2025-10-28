from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    temperature=0.7
)

model = ChatHuggingFace(llm = llm )

parser  = JsonOutputParser()
template1 = PromptTemplate(
    template= "Give name , age , qualification of tata group  ex chairman {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}

)
'''
prompt = template1.invoke({})

result = model.invoke(prompt)

final_output = parser.parse(result.content)
'''
#with chains

chains  = template1 | model | parser

result_chains = chains.invoke({})

print(result_chains)