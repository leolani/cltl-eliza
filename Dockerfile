# syntax = docker/dockerfile:1.2

FROM python:3.9

WORKDIR /cltl-eliza
COPY src requirements.txt makefile ./
COPY config ./config
COPY util ./util

RUN --mount=type=bind,target=/cltl-eliza/repo,from=cltl/cltl-requirements:latest,source=/repo \
        make venv project_repo=/cltl-eliza/repo/leolani project_mirror=/cltl-eliza/repo/mirror

CMD . venv/bin/activate && python main.py
