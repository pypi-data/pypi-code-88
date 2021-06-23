from setuptools import setup

setup(
    name="motools",
    version="0.4",
    description="modelling tools",
    packages=["motools"],
    zip_safe=False,
    install_requires=[
        "joblib==1.0.1",
        "numpy==1.19.5",
        "pandas==1.1.5",
        "pyodbc==4.0.30",
        "scikit-learn==0.23.2",
        "scipy==1.5.4",
        "tqdm==4.56.0",
        "XlsxWriter==1.3.7",
        "xgboost==1.3.3",
        "catboost==0.24.4",
        "lightgbm==3.1.1",
    ],
)
