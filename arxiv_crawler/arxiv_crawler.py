import os
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
        with open(papers_list_path, 'r', encoding = "utf8") as f:
            existing_ids = set(line.strip() for line in f)
    else:
        existing_ids = set()

    query = f"{keyword} AND (cs.LG OR cs.AI)"
    client = arxiv.Client(
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
    dir = "./papers_metadata"
    os.makedirs(dir, exist_ok = True)
    date = str(datetime.date.today()).replace("-", "")[2:]
    file_path = f"{dir}/papers_{date}.json"
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
    with open(file_path, 'w', encoding = "utf8") as file:
        json.dump(papers_metadata, file, indent = 4)
    return papers_metadata


def dict_to_md(papers_metadata):
    """
    Convert the papers metadata to a Markdown file.
    """
    file_name = "README.md"
    abstract_dir = "./papers_abstract"
    os.makedirs(abstract_dir, exist_ok = True)
    date = str(datetime.date.today())
    abstract_path = f"{abstract_dir}/abstracts_{date.replace('-', '')[2:]}.md"
    with open(file_name, 'r', encoding = "utf8") as file:
        lines = file.readlines()

    # 找到第一个二级标题的位置
    insert_index = 0
    for i, line in enumerate(lines):
        if line.startswith("## "):
            insert_index = i
            break
    insert_index = len(lines) if insert_index == 0 else insert_index

    # 插入新的二级标题
    new_content = f"\n## Update on {date}\n"

    f = open(abstract_path, 'w', encoding = "utf8")
    f.write(f"# Abstracts of Papers\n\n")
    abstracts_content = ""
    # keyword 作为三级标题
    for k, v in papers_metadata.items():
        new_content += f"\n### {k}\n"
        abstracts_content += f"## {k}\n"
        new_content += "|Publish Date|Updated Date|Title|Authors|PDF|\n"
        new_content += "|---|---|---|---|---|\n"
        for paper_metadata in v:
            published_date = paper_metadata['published'].split()[0]
            updated_date = paper_metadata['updated'].split()[0]
            title = paper_metadata['title']
            authors = paper_metadata['authors']
            pdf_url = paper_metadata['pdf_url']
            pdf_id = pdf_url.split('/')[-1]

            abstract = paper_metadata['summary']
            abstracts_content += f"### {title}\n"
            abstracts_content += f"**Authors**: {authors}\n\n"
            abstracts_content += f"**Published Date**: {published_date}\n\n"
            abstracts_content += f"**Updated Date**: {updated_date}\n\n"
            abstracts_content += f"**PDF Url**: [{pdf_id}]({pdf_url})\n\n"
            abstracts_content += f"**Abstract**: {abstract}\n\n\n"

            new_content += f"|{published_date}"
            new_content += f"|{updated_date}"
            new_content += f"|{title}"
            new_content += f"|{authors.split(', ')[0]}"
            new_content += f"|[{pdf_id}]({pdf_url})|\n"
    f.write(abstracts_content)
    f.close()

    # 更新 README.md 文件
    lines.insert(insert_index, new_content)
    with open(file_name, 'w', encoding = "utf8") as file:
        file.writelines(lines)


def json_to_md(json_path):
    """
    Convert the papers metadata in a JSON file to a Markdown file.
    """
    with open(json_path, 'r', encoding = "utf8") as file:
        papers_metadata = json.load(file)
    dict_to_md(papers_metadata)


def main():
    keywords = ["World Model", "Generation", "VLA", "Agent"]
    max_results = [6, 6, 6, 6]
    papers = {}
    for i, keyword in enumerate(keywords):
        time.sleep(30)
        try:
            papers_per_keyword = search_by_keyword(keyword, max_results[i])
            if papers_per_keyword:
                papers[keyword] = papers_per_keyword
        except Exception as e:
            print(f"Warning: Unexpected error for keyword '{keyword}': {e}")
        
    if papers:
        papers_metadata = save_to_json(papers)
        dict_to_md(papers_metadata = papers_metadata)
    else:
        print("No new papers found for any keyword.")


if __name__ == "__main__":
    main()
