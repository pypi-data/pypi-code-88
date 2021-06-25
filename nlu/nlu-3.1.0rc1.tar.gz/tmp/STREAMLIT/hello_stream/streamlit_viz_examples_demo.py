import streamlit as st
import pandas as pd
import numpy as np



"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MAP AND BART CHART BELOW @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ALTAIOR REAL TIME PLOT BELOW@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import time
# Generate some random data
df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# Build a scatter chart using altair. I modified the example at
# https://altair-viz.github.io/gallery/scatter_tooltips.html
scatter_chart = st.altair_chart(
    alt.Chart(df)
        .mark_circle(size=60)
        .encode(x='a', y='b', color='c')
        .interactive()
)

# Append more random data to the chart using add_rows
for ii in range(0, 100):
    df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    scatter_chart.add_rows(df)
    # Sleep for a moment just for demonstration purposes, so that the new data
    # animates in.
    time.sleep(0.1)

"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@3d  THINLGY BELOW https://discuss.streamlit.io/t/plotly-in-streamlit/1319/4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# from Inputs_Parallel import get_possible_scenarios

# Side Bar #######################################################
project_title = st.sidebar.text_input(label="Title of Project",
                                      value="Example Project")

username = st.sidebar.selectbox(label="Username",
                                options=("a_name",
                                         "b_name"))

buildable_land_folder = st.sidebar.text_input(label="Buildable Land Folder",
                                              value=r"\\filepath\example")

config_file_location = st.sidebar.text_input(label="Config File",
                                             value=r"\\filepath\example")

gcr_config = st.sidebar.slider(label="Ground Coverage Ratio Range Selection",
                               min_value=10,
                               max_value=60,
                               step=1,
                               value=(28, 45))

sr_config = st.sidebar.slider(label="Sizing Ratio Range Selection",
                              min_value=1.0,
                              max_value=2.0,
                              step=0.1,
                              value=(1.0, 1.5))

run_button = st.sidebar.button(label='Run Optimization')

progress_bar = st.sidebar.progress(0)

# App ###########################################################
st.title(project_title)

# Graphing Function #####
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='IRR', autosize=False,
                  width=800, height=800,
                  margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)