# About
This repository contains the source for converting
a Tensorflow 2.x SavedModel format into an `.mlmodel` format supported by CoreML in iOS 13.

## Usage
1. Place the SavedModel in the `models` directory
2. Run the Docker container `make model_name=your_model_name convert`

## License
MIT