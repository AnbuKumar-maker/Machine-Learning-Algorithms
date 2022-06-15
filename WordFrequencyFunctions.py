#CodingScientist Anbu Kumar
#Word Frequency Functions

import string
from math import log10

def term_frequency(term: str, document: str) -> int:
    """
    Return the number of times a term occurs within
    a given document.
    @params: term, the term to search a document for, and document,
            the document to search within
    @returns: an integer representing the number of times a term is
            found within the document

    @examples:
    >>> term_frequency("to", "To be, or not to be")
    2
    """
    # strip all punctuation and newlines and replace it with ''
    document_without_punctuation = document.translate(
        str.maketrans("", "", string.punctuation)
    ).replace("\n", "")
    tokenize_document = document_without_punctuation.split(" ")  # word tokenization
    return len([word for word in tokenize_document if word.lower() == term.lower()])


def document_frequency(term: str, corpus: str) -> tuple[int, int]:
    """
    Calculate the number of documents in a corpus that contain a
    given term
    @params : term, the term to search each document for, and corpus, a collection of
             documents. Each document should be separated by a newline.
    @returns : the number of documents in the corpus that contain the term you are
               searching for and the number of documents in the corpus
    @examples :
    >>> document_frequency("first", "This is the first document in the corpus.\\nThIs\
is the second document in the corpus.\\nTHIS is \
the third document in the corpus.")
    (1, 3)
    """
    corpus_without_punctuation = corpus.lower().translate(
        str.maketrans("", "", string.punctuation)
    )  # strip all punctuation and replace it with ''
    docs = corpus_without_punctuation.split("\n")
    term = term.lower()
    return (len([doc for doc in docs if term in doc]), len(docs))


def inverse_document_frequency(df: int, N: int, smoothing=False) -> float:
    """
    Return an integer denoting the importance
    of a word. This measure of importance is
    calculated by log10(N/df), where N is the
    number of documents and df is
    the Document Frequency.
    @params : df, the Document Frequency, N,
    the number of documents in the corpus and
    smoothing, if True return the idf-smooth
    @returns : log10(N/df) or 1+log10(N/1+df)
    @examples :
    >>> inverse_document_frequency(3, 0)
    Traceback (most recent call last):
     ...
    ValueError: log10(0) is undefined.
    >>> inverse_document_frequency(1, 3)
    0.477
    >>> inverse_document_frequency(0, 3)
    Traceback (most recent call last):
     ...
    ZeroDivisionError: df must be > 0
    >>> inverse_document_frequency(0, 3,True)
    1.477
    """
    if smoothing:
        if N == 0:
            raise ValueError("log10(0) is undefined.")
        return round(1 + log10(N / (1 + df)), 3)

    if df == 0:
        raise ZeroDivisionError("df must be > 0")
    elif N == 0:
        raise ValueError("log10(0) is undefined.")
    return round(log10(N / df), 3)


def tf_idf(tf: int, idf: int) -> float:
    """
    Combine the term frequency
    and inverse document frequency functions to
    calculate the originality of a term. This
    'originality' is calculated by multiplying
    the term frequency and the inverse document
    frequency : tf-idf = TF * IDF
    @params : tf, the term frequency, and idf, the inverse document
    frequency
    @examples :
    >>> tf_idf(2, 0.477)
    0.954
    """
    return round(tf * idf, 3)