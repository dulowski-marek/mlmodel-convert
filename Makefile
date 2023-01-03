image_name = dulowski-marek/mlmodel-convert
current_dir = $(shell pwd)
is_classifier = true

build:
	docker build -t $(image_name) .

convert: build
	docker run -it \
		-v $(current_dir)/models:/tmp/models \
		-v $(current_dir)/out:/tmp/out \
		-e MODEL_NAME=$(model_name) \
		-e IS_CLASSIFIER=$(is_classifier) \
		$(image_name)

clean:
	rm -rf ./out
