def convert(my_name):
    """
    Print a line about converting a notebook.
    Args:
        my_name (str): person's name
    Returns:
        None
    """

    print(f"I'll convert a notebook for you some day, {my_name}.")

class Data():
    def __init__(self) -> None:
        pass
    def add_dataset(dataset):
        print(dataset)
    def show_dataset():
        import seaborn
        return seaborn.get_dataset_names()
    def load_dataset(name):
        import seaborn
        dataset = seaborn.load_dataset(name)
        return dataset