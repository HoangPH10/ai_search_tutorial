def read_prompt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()
    return contents
