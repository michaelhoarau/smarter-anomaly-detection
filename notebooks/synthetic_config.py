# Update the name of the bucket you want to use
# to store the intermediate results of this getting
# started:

BUCKET                   = '<<YOUR_BUCKET>>'

# You can leave these other parameters to these
# default values:

PREFIX_TRAINING          = 'smarter-anomaly-detection-synth/training-data/'
PREFIX_LABEL             = 'smarter-anomaly-detection-synth/label-data/'
PREFIX_INFERENCE         = 'smarter-anomaly-detection-synth/inference-data'
DATASET_NAME             = 'synthetic'
MODEL_NAME               = f'{DATASET_NAME}-model'
INFERENCE_SCHEDULER_NAME = f'{DATASET_NAME}-scheduler'