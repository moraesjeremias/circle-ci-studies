from setuptools import setup

setup(
    name='circle-ci',
    version='0.1.0',
    packages=['src'],
    install_requires=[
        'fastapi',
        'uvicorn'
    ],
    python_requires='>=3.9'
)
