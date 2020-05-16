# base tools
import datetime, time
from concurrent.futures import ThreadPoolExecutor

# dash tools
import dash
from dash.dependencies import Input, Output
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go

# internal tools
from settings import env_variables, writer_config, scheduler_config, logger
from engineering import *
from preprocess import *
from app_logging import logger
from reading import Reader
from schedule import Scheduler

# warning
import warnings
warnings.simplefilter("ignore")

# ------------------------------ Dash app ------------------------------

app = dash.Dash()

# ------------------------------ Dash app ------------------------------

VALID_USERNAME_PASSWORD_PAIRS = {
    env_variables['app_user']: env_variables['app_password']
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS)


# ------------------------------ Globals ------------------------------

# app tools
reader = Reader(writer_config, logger, env_variables['env_mode'])
scheduler = Scheduler(scheduler_config, logger, env_variables['env_mode'])

# static data


# app DB


# dashboard globals


# scheduler globals


# ------------------------------ Data Update ------------------------------

def data_update():
    logger.info('Data Update Worker - start running')

    time.sleep(60)

    try:
        while True:
            global next_read
            now = datetime.datetime.now()

            if next_read['date'] <= now:

                logger.info('Data Update Worker - start update globals')

                next_read = scheduler.get_next_read(now)

                logger.info('Data Update Worker - finished update globals')

            time.sleep(60)

    except Exception as ex:
        logger.error(str(ex))


# ------------------------------ Helpers ------------------------------

def indicator(id, text, background_color):
    return html.Div(
        [

            html.P(
                text,
                style={'color': "white", 'font-size': '100%', 'align-text': 'center'}
            ),
            html.P(
                id=id,
                style={'font-size': '150%', 'align-text': 'center'}
            ),
        ], style={'backgroundColor': background_color, "height": "10vh", 'width': '10%'},
        className="one columns indicator pretty_container"
    )


# ------------------------------ Layout ------------------------------

def serve_layout():
    return \
    html.Div(id='entry', children=[
        dcc.Loading(id='loading', fullscreen=True,
                    children=[html.H2(id='main-title', style={'color': 'black',
                                                              'margin-top': '-0.1%', "height": "4vh"},
                                      className='twelve columns')],
                    style={'backgroundColor': 'white'}),
        html.Div(children=[], style={}, className='twelve columns'),
        dcc.Interval(
            id='interval-loading',
            interval=5 * 1000,  # in milliseconds
            n_intervals=0,
            max_intervals=0
        ),
        dcc.Interval(
            id='interval-update-globals',
            interval=60*1000  # in milliseconds
        ),
        html.Div(id='fake')
    ], style={})


app.layout = serve_layout


# ------------------------------ Callbacks ------------------------------

@app.callback(Output('main-title', 'children'),
              [Input('interval-loading', 'interval')])
def entry_update(n):
    time.sleep(n / 1000)
    return 'Dashboard Title'


@app.callback([Output('some-id', 'some-property')],
              [Input('interval-update-globals', 'n_intervals')])
def app_update(n_intervals):
    globals_tuple = ()

    return globals_tuple


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(data_update)

    app.run_server(debug=True)
