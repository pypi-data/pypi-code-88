from customer_prediction.chart.chart import plot_roc_curve
from sklearn.metrics import roc_curve, auc, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV, train_test_split
import dask_ml.model_selection as ms


def grid_search(classifier, x, y, param_grid=None, train_size=0.8, random_state=45, cv=5, n_jobs=-1, scoring='recall',
                verbose=1):
    return grid_search_common(classifier, x, y, GridSearchCV, param_grid, train_size, random_state, cv, n_jobs,
                              scoring, verbose)


def grid_search_cluster(classifier, x, y, param_grid=None, train_size=0.8, random_state=45, cv=5, n_jobs=-1,
                        scoring='recall',
                        verbose=1):
    return grid_search_common(classifier, x, y, ms.GridSearchCV, param_grid, train_size, random_state, cv, n_jobs,
                              scoring, verbose)


def grid_search_common(classifier, x, y, grid, param_grid=None, train_size=0.8, random_state=45, cv=5, n_jobs=-1,
                       scoring='recall',
                       verbose=1):
    if param_grid is None:
        param_grid = {}
    grid_search = grid(classifier, param_grid, cv=cv, n_jobs=n_jobs, scoring=scoring, verbose=verbose) if type(grid) == GridSearchCV else grid(classifier, param_grid, cv=cv, n_jobs=n_jobs, scoring=scoring)
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=train_size, random_state=random_state)
    grid_search.fit(X_train, y_train)
    y_pred = grid_search.predict(X_test)
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    print(f'Roc-curve: {auc(fpr, tpr)}')
    print(f'Report: \n {classification_report(y_test, y_pred)}')
    print(f'Confusion matrix: {confusion_matrix(y_test, y_pred)}')
    plot_roc_curve(y_test, y_pred)
    return grid_search
