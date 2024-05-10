import logging
from typing import Dict, List, Set, Union
from functools import reduce
from gliner import GLiNER


class EntityExtractorModel:

    def __init__(self, pre_trained_model_name: str, multi_label: bool, flat_ner: bool) -> None:
        self._load_entity_extractor_model(pre_trained_model_name)
        self._multi_label = multi_label
        self._flat_ner = flat_ner

    def _load_entity_extractor_model(self, pre_trained_model_name: str):
        logging.info("Loading entity extractor model from {}".format(pre_trained_model_name))
        self._model = GLiNER.from_pretrained(pre_trained_model_name)
    
    async def extract_entities(self, text: str, labels: Set[str], threshold: float = 0.5) -> List[Dict[str, Union[str, float]]]:
        logging.info("Extracting entities from {}".format(text))
        model_outputs = self._model.predict_entities(text, labels, threshold=threshold, multi_label=self._multi_label, flat_ner=self._flat_ner)
        outputs = []

        for model_output in model_outputs:
            output = dict(
                label = model_output["label"],
                text = model_output["text"],
                score = model_output["score"]
            )

            outputs.append(output)
        
        logging.info("Entites extracted from {}: {}".format(text, outputs))

        return outputs
    