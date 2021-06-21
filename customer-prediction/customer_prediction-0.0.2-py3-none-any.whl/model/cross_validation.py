from sklearn.model_selection import cross_val_score, ShuffleSplit
import numpy as np


def cross_validation(model, X_data, Y_data, cv=10, scoring='recall'):
    measure = cross_val_score(model, X_data, Y_data,
                              n_jobs=-1, cv=cv, scoring=scoring, verbose=1)
    print('Cross validation with {cv}-folds')
    print(measure)
    print(np.mean(measure))


def cross_validation_shuffle(model, X_data, Y_data, n_splits=10, scoring='recall'):
    shuffle_split = ShuffleSplit(test_size=0.5, train_size=0.5, n_splits=n_splits)
    measure = cross_val_score(model, X_data, Y_data,
                              n_jobs=-1, cv=shuffle_split, scoring=scoring, verbose=1)
    print('Cross validation shuffle with {cv}-folds')
    print(measure)
    print(np.mean(measure))
