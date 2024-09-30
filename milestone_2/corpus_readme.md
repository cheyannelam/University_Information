# Corpus README

## Overview
This documentation details the corpus collection project focused on the top 1000 universities as per the QS World University Rankings 2024. The project comprises two distinct parts: a complete corpus with the original text from the first paragraphs of Wikipedia pages, and a tokenized corpus, which is a tokenized version of the complete corpus text, preserving compound words.

## Source of the Corpus
The corpora were sourced from English Wikipedia pages corresponding to universities listed in the QS World University Rankings 2024. This ensures a high-quality, diverse dataset reflective of the global educational landscape.

## Location of the Collected Corpus
The collected corpora are hosted on our GitHub Repo:
- Complete Corpus: https://github.ubc.ca/MDS-CL-2023-24/COLX_523_zhiyang_yushun_huiyin_trang/tree/master/complete_university_corpus
- Tokenized Corpus: https://github.ubc.ca/MDS-CL-2023-24/COLX_523_zhiyang_yushun_huiyin_trang/tree/master/tokenized_corpus

## Data Processing
To ensure consistency and accessibility across the dataset, university names listed in the QS World University Rankings 2024 have been standardized. This process involves unifying the name format and converting university names from other languages (German, Spanish, French, Portuguese) to English.

## Format and Metadata
Both corpora are stored in JSON format, with each document keyed by `university_name` and containing the `text` field. The complete corpus includes the original text, while the tokenized corpus features the text in a tokenized format, with an emphasis on retaining compound words for analysis.

## Total Number of Documents
Each corpus consists of exactly 1,000 documents, representing the top 1000 universities as per the QS World University Rankings 2024.

## Total Amount of Text
- The Complete Corpus contains approximately 75,000 words.
- The Tokenized Corpus consists of approximately 55,000 tokens.

## Known Problems with the Corpus
- **Inconsistencies in Formatting**: Given the diverse nature of Wikipedia page structures, some documents may exhibit minor formatting inconsistencies.
- **Tokenization Ambiguities**: For the tokenized corpus, the process may not perfectly preserve all compound words, leading to potential issues for subsequent annotation and research.


```python

```
