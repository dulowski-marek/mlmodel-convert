import os

import coremltools as ct
import tensorflow as tf

cwd = os.getcwd()
model_name = 'Model'
model_dir = os.getenv('MODEL_DIR', model_name)
out_dir = os.getenv('OUT_DIR', 'out')

input_dir = os.path.join(cwd, 'models', model_dir)
output_file = os.path.join(cwd, out_dir, f'{model_name}.mlmodel')

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
    inputs=[ct.ImageType()]
)

ct_model.save(output_file)
