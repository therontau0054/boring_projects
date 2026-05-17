FROM python:3.10

MAINTAINER Theron Tau shilongtao@stu.pku.edu.cn

copy . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y cron

ENV CRON_SCHEDULE "0 12 * * *"
ENV KEYWORDS "world model,generation,vla,agent"
ENV MAX_RESULTS "6,6,6,6"

RUN echo "$CRON_SCHEDULE /bin/bash /app/run_arxiv_crawler.sh \"$KEYWORDS\" \"$MAX_RESULTS\"" >> /app/run_arxiv_crawler_crontab && chmod 0644 /app/run_arxiv_crawler_crontab && crontab /app/run_arxiv_crawler_crontab

CMD service cron start && streamlit run web_ui.py

EXPOSE 8501