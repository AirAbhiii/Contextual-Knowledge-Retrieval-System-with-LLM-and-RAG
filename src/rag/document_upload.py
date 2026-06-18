"""
Document upload and processing module.
"""

import os
import tempfile

from fastapi import UploadFile, File
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.rag.retriever_setup import retriever_chain
from src.tools.common_tools import enhance_description_with_llm


def documents(description: str, file: UploadFile = File(...)):
    """
    Process and upload a document for RAG.

    Validates file type, loads content, enhances description, chunks documents,
    and stores them in the vector database.

    Args:
        description: User-provided document description.
        file: The uploaded file (PDF or TXT).

    Returns:
        Boolean indicating success of the upload process.

    Raises:
        HTTPException: If file type is not supported or loading fails.
    """
    filename = file.filename
    print(filename)
    if not filename.endswith(".pdf") and not filename.endswith(".txt"):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported"
        )

    file_bytes = file.file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(filename)[1]
    ) as tmp_file:
        tmp_file.write(file_bytes)
        tmp_path = tmp_file.name

    try:
        if filename.endswith(".pdf"):
            print("Loading PDF...")
            loader = PyPDFLoader(tmp_path)
        else:
            print("Loading TXT...")
            loader = TextLoader(tmp_path, encoding="utf-8")
        
        docs = loader.load()
        print(f"Successfully loaded {len(docs)} pages/documents")
    except Exception as e:
        print(f"Error loading file: {e}")
        return False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

    try:
        # Enhance description using LLM
        print("Enhancing description with LLM...")
        description_llm = enhance_description_with_llm(description)
        print(f"Enhanced description: {description_llm}")

        # Save enhanced description
        with open("description.txt", "w", encoding="utf-8") as f:
            f.write(description_llm)
    except Exception as e:
        print(f"Error enhancing description with LLM: {e}")
        # Use original description directly if LLM fails
        print(f"Falling back to original description: {description}")
        with open("description.txt", "w", encoding="utf-8") as f:
            f.write(description)

    # Split documents into chunks
    print("Splitting documents into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    return retriever_chain(chunks)




