IMG_NAME  := docker.io/dipugodocker/quantum-img:local
HOST_PORT := 8888


@PHONY: oci-build
oci-build:
	@echo "Building OCI image..."
	@docker build -t $(IMG_NAME) . --push

@PHONY: oci-run
oci-run:
	@echo "Running OCI image..."
	@docker run --rm -it -v ${PWD}:/app --publish $(HOST_PORT):8888 --name qiskit $(IMG_NAME)

@PHONY: oci-shell
oci-shell:
	@echo "Opening shell in OCI image..."
	@docker exec -it qiskit /bin/bash

@PHONY: oci-clean
oci-clean:
	@echo "Removing OCI image..."
	@docker rm -f qiskit
	@docker rmi $(IMG_NAME)
