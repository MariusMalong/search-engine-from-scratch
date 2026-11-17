# Search Engine From Scratch — Plan

Goal: a search engine over developer documentation, from raw HTML to ranked,
measured results, then improved with semantic search, with the improvement
proven by numbers.

Corpus: Python docs HTML archive (https://docs.python.org/3/download.html).
FastAPI and pandas docs may be added later.

## Stage 0 — Corpus
- [ ] Parse each HTML page into title, URL and main text (BeautifulSoup)
- [ ] Store documents in SQLite
- [ ] Inspect output for empty pages, duplicates, odd characters

## Stage 1 — Index and boolean search
- [ ] Tokeniser: lowercase, punctuation, stopwords
- [ ] Tests for tricky tokens: `read_csv()`, `Don't`, `HTTP/2`, `3.12`
- [ ] Inverted index checked by hand on 5 tiny documents
- [ ] Index built on the full corpus
- [ ] AND queries from the CLI: `python search.py "read csv"`

## Stage 2 — Ranking
- [ ] TF-IDF scoring
- [ ] BM25 scoring (with notes on k1 and b)
- [ ] Compare the two on a handful of queries

## Stage 3 — Product layer
- [ ] FastAPI search endpoint
- [ ] Simple web search page
- [ ] Snippets with highlighted query terms
- [ ] Persist the index to disk
- [ ] Record query latency

## Stage 4 — Evaluation (do before semantic search)
- [ ] 30–50 test queries
- [ ] Correct pages marked for each
- [ ] precision@5, MRR, nDCG@10 for BM25
- [ ] Baseline numbers recorded in README

## Stage 5 — Semantic and hybrid search
- [ ] Embed documents with `sentence-transformers`
- [ ] Semantic-only search
- [ ] Hybrid BM25 + embeddings (reciprocal rank fusion)
- [ ] Compare all three against Stage 4 metrics; write up what changed

## Stretch (pick one or two)
- Polite crawler (robots.txt, rate limiting)
- Phrase queries using word positions
- Spelling correction
- PageRank over internal doc links
- Docker + deployed demo

## Out of scope
Web-scale crawling, distributed indexing, competing with Google.
