import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI, GPT4All
from _config import _config as _config_


def qa_chain(retriever):
    _config = _config_.PGConfigSingleton()
    _location = _config.config.get("model_location")
    _location = os.path.expanduser(_location) if _location.startswith("~") else _location
    return RetrievalQA.from_chain_type(
        retriever=retriever,
        llm=GPT4All(model=_location,
                    n_threads=_config.config.get("retrieval_qa_thread_count")
                    ),
        chain_type=_config.config.get("retrieval_qa_type")
    )
