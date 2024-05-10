import asyncio
import logging
import tornado

from entity_extractor_service.entity_extractor_model import EntityExtractorModel
from entity_extractor_service.service.handlers.entity_extractor_handler import EntityExtractorHandler
from entity_extractor_service.service.handlers.liveness_handler import LivenessHandler


def create_service(entity_extractor_model: EntityExtractorModel) -> tornado.web.Application:
    initialization_parameters = dict(
        entity_extractor_model=entity_extractor_model,
    )

    application = tornado.web.Application([
        (r"/extract/?", EntityExtractorHandler, initialization_parameters),
        (r"/?", LivenessHandler)
    ])

    return application


async def start_service(service: tornado.web.Application, host: str, port: int) -> None:
    logging.info("Listening on port %s:%s", host, port)
    service.listen(port, address=host)
    await asyncio.Event().wait()