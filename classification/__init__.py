from utils import tune_all_models_on_all_datasets
from classification import datasets, models

def tune_all_models_on_all_classification_datasets(tuning_trials_per_step=5, tuning_time=120):
    tune_all_models_on_all_datasets('classification', datasets.all_datasets, models.all_models,
                                    tuning_trials_per_step, tuning_time)