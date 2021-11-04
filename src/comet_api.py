import os
from comet_ml import Experiment

COMET_API_KEY = os.environ.get("COMET_API_KEY")
experiment = Experiment(COMET_API_KEY)