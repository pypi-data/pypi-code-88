import numpy as np
from config.core import config
from pipeline import price_pipe
from processing.data_manager import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split


def run_training() -> None:
    """Mentraining model kita"""

    # Membaca dataset train kita
    data = load_dataset(file_name=config.app_config.training_data_file)

    # Membagi training dan test set (menggunakan config)
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],  # predictors
        data[config.model_config.target],
        # Menentukan ukuran test set
        test_size=config.model_config.test_size,
        # Menentukan random seed agar bisa di reproduce (hasilnya sama)
        random_state=config.model_config.random_state,
    )
    y_train = np.log(y_train)

    # fit model kita
    price_pipe.fit(X_train, y_train)

    # Menyimpan (persist) model yang sudah ditraining
    save_pipeline(pipeline_to_persist=price_pipe)


if __name__ == "__main__":
    run_training()
