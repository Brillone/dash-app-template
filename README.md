*** In progress

# Introduction
This repository introduce Plotly Dash app template served with waitress.

[Plotly Dash](https://plotly.com/dash/) - The Dash platform empowers Data Science teams to focus on the data and models, while producing and sharing enterprise-ready analytic apps that sit on top of Python and R models. What would typically require a team of back-end developers, front-end developers, and IT can all be done with Dash.

[Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) - Waitress is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones which live in the Python standard library. It runs on CPython on Unix and Windows under Python 2.7+ and Python 3.4+. It is also known to run on PyPy 1.6.0 on UNIX. It supports HTTP/1.0 and HTTP/1.1.

__App use case__:

A simple live dashboard (small scale) with live data pulled by a defined schedule.
As waitress is a thread based server, data is being updated by additional thread running a long with waitress server.

The template itself includes basic logging and the structure of the data updating pipeline (reading, preprocessing, engineering).
Further, the dash app has a loading screen using [dcc.Loading] component when app starts. This is usefull when app includes havy plots, which takes long time to be loaded at app startup. To get more info, please enter dash docs.


# Getting Started
The dash_app dir contains the app template. The following steps need to be implemented by the user:
1. The dash application.
2. Reading module.
3. Preprocessing module.
4. Engineering module.
5. App assests.
6. Config files.


## 1. App Structure

dash_app/ # project dir
│
├── assets/ # app static assets
│   ├── css-design1.css
│   ├── css-design2.css
│   └── static_data/
|       ├── static_data_file.csv
│
├── __init__.py
├── app.py # the dash app implementation
├── engineering.py # engineering scripts used by the app, e.g.: plots data, plots filtering, .. 
├── preprocess.py # preprocess scripts of the data being read
├── reading.py # reading module to read data
├── schedule.py # schedule module for data updates
├── server.py # serving with waitress
├── setting.py # app configuration: logger, env vars and config file.


## 2. Examples

Currently, there is no example app. I'll upload a full example in the future.

## 3. Future

* gunicorn compatibility.
* Use in memory database instead of globals.
* multi-threading vs multi-processing.
* Dockerize app.
