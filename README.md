# About
This repository contains the source for converting
a Tensorflow 2.x SavedModel format into an `.mlmodel` format supported by CoreML in iOS 13.

## Convert a classifier

### Prepare the `.class_labels` file
In order for the model to be considered a classifier, it has to have class labels
assigned to the neural network outputs.

The class labels are stored separately from the model in a `.class_labels` file,
where each class label is defined on a new line.

For example, if the model has 3 outputs `red, green, blue`, the `.class_labels` file should contain:
```
red
green
blue
```

### Place the model and class labels in the `models` directory
The `models` directory contains the models and class labels that are used for conversion.
Note that the SavedModel folder name and the `.class_labels` file name should match.

For example, for a model named `DetectColor`, the directory name should be `DetectColor` and
the `.class_labels` file should be named `DetectColor.class_labels`.

### Convert the model
1. Run the Docker container using `make model_name=DetectColor convert` where `model_name` is the name of the model directory.
2. The docker container will be built and run the `convert.py` script.

The output of that should be `out/DetectColor.mlmodel`.

## License
MIT