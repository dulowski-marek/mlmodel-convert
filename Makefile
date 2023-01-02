image_name=dulowski-marek/mlmodel-convert
current_dir = $(shell pwd)

build:
	docker build -t $(image_name) .

convert: build
	docker run -it -v $(current_dir)/models:/tmp/models -v $(current_dir)/out:/tmp/out -e MODEL_NAME=$(model_name) $(image_name)

clean:
	rm -rf ./out