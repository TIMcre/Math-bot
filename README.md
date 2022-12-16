# Realmath Solver

This repository contains two scripts that can be used to solve math problems on the website [realmath.de](https://www.realmath.de/). The scripts use the `selenium` library to control a web browser and interact with the website.

## main.py

The `main.py` script allows you to automatically answer math problems on the website. It uses a previously gathered database of questions and answers to find the correct answer for each question.

To use the script, you will need to have the following dependencies installed:

- selenium
- pandas
- tqdm

You will also need to have the [geckodriver](https://github.com/mozilla/geckodriver/releases) executable in the same directory as the script.

To run the script, simply execute `python main.py` in the command line and follow the prompts. You will be asked to enter the number of iterations you want the script to run for. The script will then open a Firefox browser, navigate to the realmath website, and start answering math problems. The progress of the script will be displayed using a progress bar.

## update_database.py

The `update_database.py` script allows you to gather a new database of questions and answers from the realmath website. It works by generating new math problems and showing the correct answers, and then adding this data to a CSV file.

To use the script, you will need to have the same dependencies as the `main.py` script. You will also need to have an empty `data.csv` file in the same directory as the script.

To run the script, simply execute `python update_database.py` in the command line. The script will then open a Firefox browser, navigate to the realmath website, and start gathering data. The progress of the script will be displayed using a progress bar. Once the script has finished running, the new data will be appended to the `data.csv` file.

## Disclaimer

Please note that using these scripts to cheat on math problems is strictly prohibited and unethical. These scripts are intended for educational and research purposes only.

# Contributing

We welcome contributions to this repository! If you have an idea for how to improve the scripts or have found a bug, please create a fork of the repository and create a pull request with your changes. We will review the pull request and, if it is approved, merge it into the upstream repository. Thank you for your contribution!
