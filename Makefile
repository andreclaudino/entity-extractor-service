IMAGE_REGISTRY=docker.io/andreclaudino
PROJECT_VERSION := $$(cat ./pyproject.toml | grep version | head -n 1 | awk '{print $$3}' | sed -r 's/^"|"$$//g')
BINARY_NAME := $$(cat ./pyproject.toml | grep name | head -n 1 | awk '{print $$3}' | sed -r 's/^"|"$$//g')
IMAGE_NAME=$(IMAGE_REGISTRY)/$(BINARY_NAME):$(PROJECT_VERSION)


flags:
	mkdir -p flags/

flags/login: flags
	podman login docker.io
	touch flags/login

flags/build: flags
	pyclean .
	podman build . -f docker/Dockerfile -t $(IMAGE_NAME)
	touch flags/build

flags/push: flags/login flags/build
	podman push $(IMAGE_NAME)
	touch flags/push

clean:
	rm -rf flags/
