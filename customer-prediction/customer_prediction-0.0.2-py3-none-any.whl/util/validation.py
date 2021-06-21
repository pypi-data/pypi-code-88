import numpy as np

# проверка что в колонке в которой нужны уникальные значения (например id) все значения уникальны
def check_unique_values_on_field(df, field):
    return df[field].unique().shape[0] == df.shape[0]


# проверка что в колонке в тестовой и тренировочной выборке значения совпадают
def check_that_values_are_the_same(train_df, test_df, field):
    return np.array_equal(np.sort(train_df[field].unique()), np.sort(test_df[field].unique()))
