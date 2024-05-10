# Entity extractor service

A service for named entity extraction using GliNER

## Usage

```SHELL
podman run docker.io/andreclaudino/entity-extractor-service:1.0.0 --help


Options:
  --port INTEGER                  Porta where HTP service will listen for
                                  requests
  --host TEXT                     Host onde o servidor HTTP escuta requisições
  --model-name TEXT               Model to for entity recognition  [required]
  --log-level [DEBUG|INFO|WARNING|ERROR|CRITICAL]
                                  Nível de log a ser reportado durante a
                                  execução
  --multi-label / --single-label
  --flat-ner / --nested-ner
  --help                          Show this message and exit.
```

## Helm chart

On the helm chart, values are:

```SHELL
--model-name => modelName
--log-level => logLevel
```
