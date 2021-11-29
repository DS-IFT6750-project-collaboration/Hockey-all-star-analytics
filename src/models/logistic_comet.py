# import comet_ml at the top of your file
from comet_ml import Experiment

# Create an experiment with your api key
experiment = Experiment(
    project_name="hockey-all-star-analytics",
    workspace="zilto",
)
path = "/Users/henaghonia/Desktop/udem/Sem-1/Data-science/Hockey-all-star-analytics/models/"

experiment.log_model("Logistic regression with distance feature only", path+"logistic_dist.sav")
experiment.log_model("Logistic regression with angle feature only", path+"logistic_angle.sav")
experiment.log_model("Logistic regression with distance and angle feature ", path+"logistic_angle_dist.sav")
experiment.end()
