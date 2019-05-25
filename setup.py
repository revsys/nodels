from setuptools import setup, find_packages

setup(
    name="nodels",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click==7.0",
        "kubernetes==9.0.0",
        "ipython==7.5.0",
        "boto3==1.9.154",
    ],
    entry_points="""
        [console_scripts]
        nodels=nodels.cli:cli
    """,
)
