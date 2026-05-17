import os
import sys
import json
import arxiv
import datetime
import requests
from bs4 import BeautifulSoup


def id_filter(id_list, max_results):
    """
    Filter the papers by the doi.
    """
    papers_list_path = "./entry_id.list"
    if os.path.exists(papers_list_path):
        with open(papers_list_path, 'r', encoding = "utf8") as f:
            id_filtered = f.readlines()
        id_filtered = [id.strip() for id in id_filtered]
    else:
        id_filtered = []
    id_new = []
    with open(papers_list_path, 'a', encoding = "utf8") as f:
        for id in id_list:
            if len(id_new) == max_results:
                break
            if id not in id_filtered:
                f.write(id + "\n")
                id_new.append(id)
    return id_new


def search_by_keyword(keyword: str, max_results: int):
    """
    Search arXiv by keyword and return the results.
    """
    assert max_results < 200, "too much and you cannot read them all!"
    keyword += " AND %28cs.LG OR cs.AI%29"
    keyword = '+'.join(keyword.split())
    url = f"https://arxiv.org/search/?searchtype=all&query={keyword}&abstracts=show&size=25&order=-submitted_date"
    id_list = []
    try:
        response = requests.get(url, timeout = 30)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            p_tags = soup.find_all('p', class_ = "list-title is-inline-block")
            if not p_tags:
                print(f"Warning: No results parsed from arXiv search page for keyword '{keyword}'")
            for i, p_tag in enumerate(p_tags):
                a_tag = p_tag.find('a')
                if a_tag:
                    a_text = a_tag.text
                    print(a_text)
                    id_list.append(a_text.split(':')[-1])
        else:
            print(f"Warning: arXiv search returned status {response.status_code} for keyword '{keyword}'")
    except Exception as e:
        print(f"Warning: Failed to fetch arXiv search results for keyword '{keyword}': {e}")

    print(id_list)
    id_list = id_filter(id_list, max_results)
    if not id_list:
        print(f"No new papers for keyword '{keyword}', skipping.")
        return []
    client = arxiv.Client()
    search = arxiv.Search(
        query = "",
        id_list = id_list,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.LastUpdatedDate
    )
    return list(client.results(search))


def get_paper_authors(paper):
    authors = []
    for author in paper.authors:
        authors.append(author.name)
    authors = ", ".join(authors)
    return authors


def save_to_json(papers):
    """
    Save the papers to a JSON file.
    """
    metadata_dir = "./papers_metadata"
    os.makedirs(metadata_dir, exist_ok = True)
    date = str(datetime.date.today()).replace("-", "")[2:]
    file_path = f"{metadata_dir}/papers_{date}.json"
    papers_metadata = {}
    for k, v in papers.items():
        papers_metadata[k] = []
        for paper in v:
            paper_metadata = {
                "title": paper.title,
                "authors": get_paper_authors(paper),
                "summary": paper.summary,
                "pdf_url": paper.pdf_url,
                "published": str(paper.published),
                "updated": str(paper.updated),
            }
            papers_metadata[k].append(paper_metadata)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding = "utf-8") as f:
            old_data = json.load(f)
        for k, v in old_data.items():
            if k in papers_metadata:
                papers_metadata[k] += v
            else:
                papers_metadata[k] = v

    with open(file_path, 'w', encoding = "utf8") as file:
        json.dump(papers_metadata, file, indent = 4)
    return papers_metadata


def get_papers_metadata(keywords, max_results):
    papers = {}
    for i, keyword in enumerate(keywords):
        papers_per_keyword = search_by_keyword(keyword, max_results[i])
        if papers_per_keyword:
            papers[keyword] = papers_per_keyword
    if papers:
        save_to_json(papers)
    else:
        print("No new papers found for any keyword.")


if __name__ == "__main__":
    keywords = sys.argv[1].split(',')
    max_results = list(map(int, sys.argv[2].split(',')))
    print(keywords, max_results)
    get_papers_metadata(keywords, max_results)
