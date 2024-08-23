#!/usr/bin/env python

import base64

from typing import Any, Callable, Dict, Union

from fastapi import FastAPI, HTTPException, Request
from langchain_core import __version__
from langchain_core.runnables import ConfigurableFieldSpec,RunnableLambda, RunnableParallel
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.document_loaders import Blob
from langchain_community.document_loaders.parsers.pdf import PDFMinerParser

from langserve import CustomUserType, add_routes
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10000, chunk_overlap=200, add_start_index=True
)
from app.chain import get_chain


# Define the minimum required version as (0, 1, 0)
# Earlier versions did not allow specifying custom config fields in
# RunnableWithMessageHistory.
MIN_VERSION_LANGCHAIN_CORE = (0, 1, 0)

# Split the version string by "." and convert to integers
LANGCHAIN_CORE_VERSION = tuple(map(int, __version__.split(".")))

if LANGCHAIN_CORE_VERSION < MIN_VERSION_LANGCHAIN_CORE:
    raise RuntimeError(
        f"Minimum required version of langchain-core is {MIN_VERSION_LANGCHAIN_CORE}, "
        f"but found {LANGCHAIN_CORE_VERSION}"
    )




app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)


chain = get_chain()





class FileProcessingRequest(CustomUserType):
    file: bytes = Field(..., extra={"widget": {"type": "base64file"}})
    num_chars: int = 100

import json
def process_file(request: FileProcessingRequest) -> str:
    """Extract the text from the first page of the PDF."""
    text = request.file
    if not isinstance(text, bytes):
        text = request.file.encode('utf-8')
    content = base64.decodebytes(text)
    print(content)
    blob = Blob(data=content)
    docs = list(PDFMinerParser().lazy_parse(blob))
    chunks = text_splitter.split_documents(docs)
    # Iterate through the chunks and process each one
    extracted_data = {}
    for chunk in chunks:
        response = chain.invoke({"text": chunk})
        # Parse JSON response and merge with existing data
        chunk_data = json.loads(response.content)
        extracted_data.update(chunk_data)
    print(extracted_data)
    return json.dumps(extracted_data, indent=4)


add_routes(
    app,
    RunnableLambda(process_file).with_types(input_type=FileProcessingRequest),
    config_keys=["configurable"],
    path="/pdf",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001)
