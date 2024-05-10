import datetime
import logging
import tornado

from entity_extractor_service.entity_extractor_model import EntityExtractorModel
from entity_extractor_service.service.handlers.json_handler import JSONHandler
from entity_extractor_service.service.handlers.request_body import RequestBody


TEXT_FIELD = "text"
LABELS_FIELD = "labels"


class EntityExtractorHandler(JSONHandler):
    def initialize(self, entity_extractor_model: EntityExtractorModel) -> None:
        super()._initialize()
        self._model = entity_extractor_model

    
    async def post(self):
        logging.debug("Received request post request")
        request_body_content = tornado.escape.json_decode(self.request.body)
        request_body = RequestBody(**request_body_content)

        logging.info("Request body is {}".format(request_body))
        
        error_messages = request_body.check_errors()
        
        if error_messages:
            concatenated_error_messages = '\n'.join(error_messages)
            logging.warning("Payload received is incorrect: for {}: {}".format(request_body, concatenated_error_messages))
            self.send_error(400, message=concatenated_error_messages)
            return

        exractions = await self._model.extract_entities(request_body.text, request_body.labels, request_body.threshold) 

        self.write_json(exractions)
