############# !huggingface-cli login ################# IMPORTANT

from langchain import HuggingFacePipeline
import transformers
import torch
import subprocess

import os

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token = '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')
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", token = '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')


pipeline = transformers.pipeline(
    "text-generation", #task
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    max_length=1000,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id
)

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})



from langchain import PromptTemplate,  LLMChain

template = input("Enter your question: ")

prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

text = '''Cricket, a bat-and-ball sport, originated in England during the 16th century. Its history is marked by its evolution from a rural pastime to a global phenomenon. In the 18th century, it gained popularity, and the first recorded cricket match took place in 1744. The Marylebone Cricket Club (MCC) established the Laws of Cricket in 1788, shaping the game's rules. The 19th century saw cricket's expansion to Australia and beyond, leading to the first-ever Test match in 1877. Cricket became an integral part of British colonialism and later gave birth to limited-overs formats. Today, it's a major global sport, with international tournaments like the ICC Cricket World Cup and T20 World Cup.'''


print(llm_chain.run(text))




