import os
import sys
import json
import time
import arxiv
import datetime


def search_by_keyword(keyword: str, max_results: int):
    """
    Search arXiv by keyword and return new papers not seen before.
    """
    papers_list_path = "./entry_id.list"
    if os.path.exists(papers_list_path):
        with open(papers_list_path, 'r', encoding="utf8") as f:
            existing_ids = set(line.strip() for line in f)
    else:
        existing_ids = set()

    query = f"{keyword} AND (cs.LG OR cs.AI)"
    client = client = arxiv.Client(
        page_size = 50,
        delay_seconds = 30.0, 
        num_retries = 3
    )
    search = arxiv.Search(
        query = query,
        max_results = max_results * 5,
        sort_by = arxiv.SortCriterion.SubmittedDate,
        sort_order = arxiv.SortOrder.Descending
    )

    try:
        results = list(client.results(search))
    except arxiv.HTTPError as e:
        print(f"Warning: arXiv API returned HTTP {e.status} for keyword '{keyword}', skipping.")
        return []
    except Exception as e:
        print(f"Warning: Failed to fetch from arXiv API for keyword '{keyword}': {e}")
        return []

    new_papers = []
    with open(papers_list_path, 'a', encoding = "utf8") as f:
        for paper in results:
            paper_id = paper.entry_id.split('/')[-1][:-2]
            if paper_id not in existing_ids:
                f.write(paper_id + "\n")
                existing_ids.add(paper_id)
                new_papers.append(paper)
                print(f"arXiv:{paper_id}")
                if len(new_papers) >= max_results:
                    break

    print([paper.entry_id.split('/')[-1][:-2] for paper in new_papers])
    if not new_papers:
        print(f"No new papers for keyword '{keyword}', skipping.")
    return new_papers


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
        try:
            papers_per_keyword = search_by_keyword(keyword, max_results[i])
            if papers_per_keyword:
                papers[keyword] = papers_per_keyword
        except Exception as e:
            print(f"Warning: Unexpected error for keyword '{keyword}': {e}")
        if i < len(keywords) - 1:
            time.sleep(5)
    if papers:
        save_to_json(papers)
    else:
        print("No new papers found for any keyword.")


if __name__ == "__main__":
    keywords = sys.argv[1].split(',')
    max_results = list(map(int, sys.argv[2].split(',')))
    print(keywords, max_results)
    get_papers_metadata(keywords, max_results)
