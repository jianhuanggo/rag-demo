from _task import question_answering as qa


def main(query: str, filepath: str) -> str:
    return qa.run(query, filepath)


if __name__ == "__main__":
    main(query="what is Question-answering (Q&A)?", filepath="/docs/question_answering.txt")

