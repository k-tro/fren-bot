from setuptools import setup, find_packages

setup(
    name="whatsapp_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "sqlite-utils"
    ],
)
