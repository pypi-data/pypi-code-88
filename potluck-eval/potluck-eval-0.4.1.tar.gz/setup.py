import setuptools

with open("README.md", 'r', encoding="utf-8") as fin:
    long_desc = fin.read()

setuptools.setup(
    name="potluck-eval",
    version="0.4.1",
    requires=["jinja2", "pygments", "flask", "flask_cas"],
    python_requires=">=3.6", # f-strings are used
    provides=["potluck", "potluck_server"],
    url="https://cs.wellesley.edu/~pmwh/potluck/docs/",
    description=(
        "Python code evaluation system and submissions server capable"
        " of unit tests, tracing, and AST inspection. [broken]"
    ),
    author="Peter Mawhorter",
    author_email="pmawhorter@gmail.com",
    packages=["potluck", "potluck_server"],
    package_data={
        "potluck": [
            "templates/rubric_evaluation.html",
            "templates/report.html",
            "resources/potluck.css",
            "resources/potluck.js",
        ],
        "potluck_server": [
            "potluck.wsgi",
            "config.py.example",
            "Makefile",
            "static/potluck.css",
            "static/potluck.js",
            "templates/base.html",
            "templates/dashboard.html",
            "templates/error.html",
            "templates/feedback.html",
            "templates/gradesheet.html",
            "templates/rubric_task.html",
            "templates/solution.html",
            "templates/extension_manager.html",
        ]
    },
    scripts=["scripts/potluck_eval"],
    # Note: MANIFEST.in grafts entire potluck_testarea directory
    license="BSD 3-Clause License",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Flask",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Education",
    ],
    long_description=long_desc,
    long_description_content_type="text/markdown"
)
