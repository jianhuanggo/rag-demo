<br>

# Welcome to Rag demo👋

**Demo for RAG (Retriever-Augmented Generation) Flow**

This project introduces a Retriever-Augmented Generation (RAG) system designed to perform sophisticated question-answering tasks. The unique feature of this system is its ability to incorporate user-uploaded documents into the LLM's memory. This enhancement allows for a more personalized and context-rich interaction, as the model can retrieve information from a specific set of documents provided by the user, making it highly relevant and accurate for specialized queries.

## Installation

Open a terminal and run:

```bash
$ pip install -r requirements.txt

```

download gpt4all model at https://gpt4all.io/index.html and specify the llm location in the config.yaml file

```python
model_location: /llm/gpt4all-falcon-q4_0.gguf

```

## Quickstart

### A little example

upload a file and start perform answer and questioning with the following code:
```python
from _task import question_answering as qa


def main(query: str, filepath: str) -> str:
    return qa.run(query, filepath)

if __name__ == "__main__":
    main(query="what is Question-answering (Q&A)?", filepath="/docs/question_answering.txt")

```
