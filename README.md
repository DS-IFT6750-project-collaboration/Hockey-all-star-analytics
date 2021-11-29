Hockey-all-star-analytics
==============================

This project is part IFT6758- Data science course taught at University of Montreal.
It contains files for data preparation and data visualization for Hockey primer using NHL data.
For Milestone 2: Refer notebooks:
                              -ift6758-milestone2_tj.ipynb  
                              -Milestone2_Q6 advanced models.ipynb
                              -Milestone2_Feature engineering(Q2,Q3).ipynb          
                              
Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Pickle file for saved models
    │
    ├── notebooks          <- Contains Jupyter notebooks for milestone 1. 
    │                         
    │                         
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── best_model.py - To logg lgbm model in comet.ml
    │   │   └── logistic_comet.py - To logg logistic regression model in comet.ml
    |   |   └── logistic_regression.py - contains code for logistic regression
    │   |   └── xgboost.py       - Contains code for xgboost model
    |   |
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
