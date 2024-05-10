FROM python:3.10

WORKDIR /application

ADD pyproject.toml /application/pyproject.toml
ADD entity_extractor_service /application/entity_extractor_service
ADD README.md /application/README.md

RUN pip install -e /application/

ENTRYPOINT [ "python", "entity_extractor_service/main.py" ]