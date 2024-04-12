import os

from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

import logging

logger = logging.getLogger("listen")

template = """Remove corrupted sentences, bad characters, and hard to read pieces in the text included between <start_listen> and <stop_listen> tags:
<start_listen>
{question}
<stop_listen>

Don't include <start_listen> or <stop_listen> in the answer, and make things easier to read and hear.
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = OpenAI(openai_api_key=os.environ.get("OPENAI_TOKEN"))
llm_chain = LLMChain(prompt=prompt, llm=llm)


def clean_text(text: str):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=2000, chunk_overlap=0, keep_separator=False)
    texts = text_splitter.split_text(text)
    cleaned_text = []
    for i, text in enumerate(texts):
        logger.info(f"Processing chunk (TXT CLEANUP) {i+1} of {len(texts)}, chunk size is {len(text)}")
        cleaned_text.append(llm_chain.invoke(text).get("text"))
    return ". ".join(cleaned_text)
