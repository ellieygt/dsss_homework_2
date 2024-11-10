from setuptools import setup, find_packages

setup(
    name="math_quiz", 
    version="0.1",
    packages=find_packages(),
    install_requires=[],  

    # Metadata
    author="Elnaz Yaghouti",
    author_email="yghelnaz@gmail.com",
    description="A simple math quiz game",
    license="Apache License 2.0",
    url="https://github.com/elnazyaghouti/dsss_homework_2",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  
        ],
    },
)
