# Common Word Checker

A script that checks if a Word document only contains the 1000 most common English words. The words are courtesy of [Education First](https://www.ef.com/wwen/english-resources/english-vocabulary/top-1000-words/).

# Getting Started
Go to the root directory of the project, `word-checker/`, and execute the following steps. 

## Set up your environment

1. Ensure you have Python 3 installed. You can check your Python version using the following command:
```
$ python --version
```

2. Set up and activate a virtual environment.
```
$ python -m venv env
$ source env/bin/activate
```

## Install the dependencies

Install the dependencies in the `requirements.txt` file.
```
$ pip install -r requirements.txt
```

## Add your test file

Add the Word document that you want to check to the root directory, `word-checker/`.

## Run the script

```
$ python word_checker.py
```

You will be prompted to enter your file name. If you leave this empty, the test file will be used.
```
$ python word_checker.py
Please enter the file name:
```

Sample output:
```
File name is empty. Using default test file.

Here are the rare words in your file:
Word: quick 	 | Occurences: 1
Word: brown 	 | Occurences: 1
Word: fox 	 | Occurences: 1
Word: jumped 	 | Occurences: 1
Word: lazy 	 | Occurences: 1
```
