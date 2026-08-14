import bibtexparser
import requests


def resolve_doi(doi):
    resp = requests.get(f"https://doi.org/{doi}", timeout=15)
    resp.raise_for_status()
    return resp.url


def format_citation(entry):
    authors = entry.get("author", "").replace(" and ", ", ")
    return f"{authors} ({entry.get('year', 'n.d.')}). {entry.get('title', '')}."


def load_bib(path):
    with open(path) as fh:
        return bibtexparser.load(fh).entries
