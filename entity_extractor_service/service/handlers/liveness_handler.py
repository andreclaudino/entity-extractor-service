import logging
from entity_extractor_service.service.handlers.json_handler import JSONHandler


class LivenessHandler(JSONHandler):
    async def get(self):
        logging.info("Answering liveness request")
        liveveness_response = dict(alive=True)
        self.write_json(liveveness_response)
