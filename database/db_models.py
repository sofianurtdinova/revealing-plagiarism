from pydantic import BaseModel


class PlagiarismCheck(BaseModel):
    """
    Checking plagiarism model.
    """

    original_text: str
    checked_text: str
    similarity: float
    rewritten_text: str|None = None


class SynonymEntry(BaseModel):
    """
    Synonyms model.
    """

    word: str
    synonym: str
