import os

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

template = """Could you remove corrupted sentence and wrong characters in the text included between <start_listen> and <stop_listen> tags: 
<start_listen>
{question}
<stop_listen>

Don't include <start_listen> or <stop_listen> in the answer.
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI(openai_api_key=os.environ.get("OPENAI_TOKEN"))
llm_chain = LLMChain(prompt=prompt, llm=llm)


def clean_text(text: str):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=0, keep_separator=False
    )
    texts = text_splitter.split_text(text)

    return ". ".join([llm_chain.run(t) for t in texts])
