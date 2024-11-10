from setuptools import setup, find_packages

setup(
    name="math_quiz",  # This should be unique to avoid conflicts on PyPI
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here or specify in requirements.txt

    # Metadata
    author="Elnaz Yaghouti",
    author_email="yghelnaz@gmail.com",
    description="A simple math quiz game",
    license="Apache License 2.0",
    url="https://github.com/elnazyaghouti/dsss_homework_2",  # Replace with your repo link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # This allows running `math_quiz` from the terminal
        ],
    },
)
