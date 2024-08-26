#!/usr/bin/env python

from typing import Any, Callable, Dict, Union

from fastapi import FastAPI, HTTPException, Request
from langchain_core.runnables import RunnableLambda
from langchain_community.document_loaders import WebBaseLoader
from langserve import  add_routes
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10000, chunk_overlap=200, add_start_index=True
)

from app.chain import get_chain
import app.checker
from typing_extensions import TypedDict
from langchain.tools.playwright import ExtractHyperlinksTool, NavigateTool
from playwright.sync_api import sync_playwright


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)

class InputChat(TypedDict):
    """Input for the chat endpoint."""

    web: str
chain = get_chain()

import json

import requests
from bs4 import BeautifulSoup

def process_file(request: InputChat) -> str:
    """Extract the text from the first page of the PDF."""
    # Initialize the tools
    # Initialize Playwright
    # reqs = requests.get(request["web"])
    # soup = BeautifulSoup(reqs.text, 'html.parser')
    # print(soup)
    # urls = []

    print("Extracting all URLs from base url")
    loader = WebBaseLoader(request["web"])
    base_content = loader.scrape()
    urls = []
    for link in base_content.find_all('a'):
        urls.append(link.get('href'))
    print(f"Found the following urls {urls}")
    docs = []
    for url in urls:
        print(f"Processing URL: {url}")
        try:
            sub_loader =  WebBaseLoader(url)
            content = sub_loader.load()[0].page_content
            content = content.replace("\n","").strip()
            content = f"url: {url}\n"+content
            docs.append(content)
        except Exception as e:
            print(f"Impossible load {url}. Error code {e}")
    # chunks = text_splitter.split_documents(docs)
    # print("Chunks created")
    # Iterate through the chunks and process each one
    extracted_data = {}
    for chunk in docs:
        response = chain.invoke({"text": chunk})
        print(response)
        # Parse JSON response and merge with existing data
        chunk_data = json.loads(response.content)
        extracted_data.update(chunk_data)
    print(extracted_data)
    return json.dumps(extracted_data, indent=4)


add_routes(
    app,
    RunnableLambda(process_file).with_types(input_type=InputChat),
    config_keys=["configurable"],
    path="/web",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001)
