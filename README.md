# diario-oficial-rag

Question answering over official gazettes: the project downloads the publications, extracts the information buried in the text and lets you ask about it in plain language.

> **Status:** work in progress. This is a learning project — the goal is to get the whole flow running end to end.

---

## The problem

Official gazettes are public, but they are published as one continuous block of text, with no consistent formatting. Finding a specific appointment, contract or decision means reading page after page by hand.

This project turns that raw text into something searchable.

---

## How it works

1. **Collection** — downloads the publications and stores the raw text
2. **Extraction** — identifies structured fields (dates, names, act number, category) using regular expressions
3. **Splitting and indexing** — breaks the text into smaller passages and stores each one in a vector database, which allows searching by meaning and not only by exact wording
4. **Answering** — retrieves the passages related to the question and hands them to the language model, which writes the answer citing the source publication

Steps 2 and 3 are what make step 4 reliable: the model answers only from the text that was retrieved, instead of making things up.

---

## Technologies

| | |
| --- | --- |
| Language | Python |
| API | FastAPI |
| Vector database | Qdrant |
| Container | Docker |

---

## Roadmap

- [ ] Collection and storage of the raw text
- [ ] Field extraction with regex
- [ ] Text splitting and indexing in the vector database
- [ ] Search endpoint
- [ ] Question answering endpoint with source citation
- [ ] Docker setup
- [ ] Tests

---

## Running locally

Instructions go here once the first version is running end to end.

---

## Structure

```
app/
├── main.py             FastAPI application
├── config.py           settings read from .env
├── api/
│   └── v1/
│       ├── search.py           passage search
│       ├── questions.py        question and answer
│       └── conversations.py    conversation history
├── models/
│   └── conversation.py     conversation and message tables
├── schemas/            API input and output formats
├── services/
│   ├── collection.py       downloads the publications
│   ├── extraction.py       extracts fields with regex
│   ├── indexing.py         splits the text and indexes it in Qdrant
│   └── answering.py        builds the answer with the LLM
└── db/
    ├── session.py          connection to the relational database
    └── qdrant.py           connection to the vector database

tests/
```

The files in `services` follow the steps of the process, not entities — each one is a piece of the pipeline described in "How it works".

---

## License

MIT
