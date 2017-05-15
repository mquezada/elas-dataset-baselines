# -*- coding: utf-8 -*-

import re
import string

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm
import unicodedata


def remove_accents(s: str) -> str:
    return unicodedata.normalize('NFKD', s) \
        .encode('ASCII', 'ignore') \
        .decode('utf-8')


def preprocess_fundamentos(documents, stem=True, lower=True):
    if lower:
        texts = [doc.fundamento.lower() for doc in documents]
    else:
        texts = [doc.fundamento for doc in documents]

    modo = [remove_accents(doc.modo.lower().strip()) for doc in documents]
    le = LabelEncoder()
    le.fit(modo)
    y = le.transform(modo)

    stemmer = SnowballStemmer(language='spanish')
    processed_texts = []

    for text in tqdm(texts):
        text_wo_nl = ' '.join(text.split())
        tokens = text_wo_nl.split()

        proc = []

        for token in tokens:
            if token in string.punctuation:
                continue
            if token in stopwords.words('spanish'):
                continue
            if re.findall(r'^[^\w\s]+$', token):
                continue

            token = token.translate({ord(k): "" for k in string.punctuation})
            token = token.strip()

            if stem:
                token = stemmer.stem(token)

            if len(token) < 2:
                continue

            proc.append(token)

        processed_texts.append(proc)

    v = TfidfVectorizer(analyzer='word', tokenizer=lambda x: x, lowercase=False)
    X = v.fit_transform(processed_texts)

    return X, processed_texts, y, le
