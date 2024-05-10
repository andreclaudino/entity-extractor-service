import asyncclick as click
import asyncio
import logging

from entity_extractor_service.constants import AVAILABLE_LOG_LEVELS, DEFAULT_LOG_LEVEL
from entity_extractor_service.entity_extractor_model import EntityExtractorModel
from entity_extractor_service.service.factory import create_service, start_service

@click.command()
@click.option("--port", default=8080, type=click.INT, envvar="PORT", help="Porta where HTP service will listen for requests")
@click.option("--host", default="0.0.0.0", type=click.STRING, envvar="HOST", help="Host onde o servidor HTTP escuta requisições")
@click.option("--model-name", type=click.STRING, envvar="MODEL_NAME", required=True, help="Model to for entity recognition")
@click.option("--log-level", envvar="LOG_LEVEL", default=DEFAULT_LOG_LEVEL, type=click.Choice(choices=AVAILABLE_LOG_LEVELS,
                                                                                              case_sensitive=False),
              help="Nível de log a ser reportado durante a execução")
@click.option("--multi-label/--single-label", type=click.BOOL, envvar="MULTI_LABEL", default=False)
@click.option("--flat-ner/--nested-ner", type=click.BOOL, envvar="FLAT_NER", default=False)
async def main(port: int, host: str, model_name: str, log_level: str, multi_label: bool, flat_ner: bool) -> None:
    logging.basicConfig(encoding='utf-8', level=log_level)
    
    entity_recognition_model = EntityExtractorModel(model_name, multi_label, flat_ner)
    service = create_service(entity_recognition_model)

    await start_service(service, host, port)


if __name__ == "__main__":
    asyncio.run(main.main())