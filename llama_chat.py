# -*- coding: utf-8 -*-
"""LLAMA_Chat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16FWNElxyFzQGaX7brphO8gfnM2F7N8ot
"""

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFacePipeline

msg = {

    SystemMessage(content="XXX")
    HumanMessage(content="YYY")
}

chat_model =  ChatHuggingFace(llm = llm)

model_template = tokenizer.chat_template

chat_model._to_chat_prompt(msg)

res = chat_model.invoke(msg)