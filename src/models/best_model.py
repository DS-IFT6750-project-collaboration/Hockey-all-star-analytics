# import comet_ml at the top of your file
from comet_ml import Experiment

# Create an experiment with your api key
experiment = Experiment(
    project_name="hockey-all-star-analytics",
    workspace="zilto",
)
path = "/Users/henaghonia/Desktop/udem/Sem-1/Data-science/Hockey-all-star-analytics/models/"

experiment.log_model("Best model-LightGBM", path+"lgbm.sav")
experiment.log_model("MLP", path+"MLP.sav")
experiment.log_model("Random forest", path+"randomForest.sav")
experiment.end()
