# Financial Crisis Scenario Analysis Application

## Introduction
Application performs analysis on a portfolio to estimate impact of a repeat of the 2008 Financial Crisis. This 'Scenario Analysis' accepts the user's portfolio holdings as input and calculates market decline based on historical returns. The application calculates expected decline using the peak-to-trough market decline in 2008 in juncture with the beta of the user's portfolio. Expected recovery time is also calculated, using historical returns following the 2008 market bottom. 

## Installation

After cloning the repository, set up a virtual environment

```
python3 -m venv my_env
```
```
source finance_env/bin/activate
```
Once environment is activated, install requirements

```
pip install -r requirements.txt
```
Run application 
```
export FLASK_APP=run.py
flask run
```

Application will be running at [http://127.0.0.1:5000](http://127.0.0.1:5000/)

## Technologies
 * Python
 * Flask
 * Jinja Templating
 * HTML
 * Bootstrap (for styling)
 
 
## Deployment
Deployed using AWS EC2. Deployed at [3.131.83.225](http://3.131.83.225/)
 
