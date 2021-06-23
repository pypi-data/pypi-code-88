from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
        name ='nepal_stonks',
        version ='0.421.69',
        author ='Buddha Gautam',
        author_email ='buddhagautam231@gmail.com',
        url ='https://github.com/buddha231/NEPALSTONKS',
        description ='Complete NepalStock solution in command line',
        long_description =long_description,
        long_description_content_type='text/markdown',
        # package_dir={"": "nepal_stonks"},
        packages=['nepal_stonks'],
        entry_points ={
            'console_scripts': [
                'priceof = nepal_stonks.priceof:main'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3",
        keywords ='nepalstock stonk buddha python package buddha69',
        install_requires = requirements,
        include_package_data=True,
        zip_safe=False,
)
