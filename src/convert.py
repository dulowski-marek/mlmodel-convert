import os

import coremltools as ct
import tensorflow as tf


cwd = os.getcwd()
models_dir = os.path.join(cwd, 'models')
out_dir = os.getenv('OUT_DIR', 'out')

model_name = os.getenv('MODEL_NAME')

input_dir = os.path.join(models_dir, model_name)
output_file = os.path.join(cwd, out_dir, f'{model_name}.mlmodel')


def is_classifier():
    return os.getenv('IS_CLASSIFIER', 'false').lower() == 'true'


def get_class_labels(model_name=model_name):
    try:
        with open(os.path.join(models_dir, f'{model_name}.class_labels')) as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError('Model is a classifier, but models/{model_name}.class_labels file does not exist')


def maybe_get_classifier_config(model_name=model_name):
    if is_classifier():
        print('Converting to classifier...')

        class_labels = get_class_labels(model_name)

        print(f'Class labels for model {model_name} are: {class_labels}')

        return ct.ClassifierConfig(class_labels)

    print('Model is not a classifier')
    return None


# Load the model in a SavedModel format (directory, Tensorflow 2.x)
tf_model = tf.keras.models.load_model(input_dir)

# Convert the model
ct_model = ct.convert(
    tf_model,
    # This will output a CoreML model (.mlmodel), which is available on iOS 13,
    # instead of a CoreML package (.mlpackage)
    convert_to='neuralnetwork',
    # Explicitly specify source as the tool cannot infer it from the model (missing metadata issue?)
    source='tensorflow',
    # Override the default input shape inferred from the model,
    # so that the model can be used with native image object.
    inputs=[ct.ImageType()],
    classifier_config=maybe_get_classifier_config(model_name)
)

ct_model.save(output_file)
