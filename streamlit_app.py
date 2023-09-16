import streamlit as st
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

data_path = Path("nesda.csv")

#st.title("Live only during presentation")
st.title("NeSDA Dashboard - Himachal Pradesh V1.0")

@st.cache_data
def load_data(path:Path) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data....')
# Load 10,000 rows of data into the dataframe.
data = load_data(data_path)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data....done!')


deptartment = st.selectbox(
    'Select the Department',
    data['Department'].unique())

options_services = st.selectbox(
    'Select the Service',
    data[data['Department']==deptartment]['Services'].unique())

nesda_param = st.selectbox(
    "Select the NeSDA Parameter",
    data[data['Department']==deptartment]['nesda_parameter'].unique()
)

filtered_data = data[data['Department']==deptartment][data['Services'] == options_services][data['nesda_parameter']==nesda_param]

transposed_data = filtered_data.T
transposed_data = transposed_data.reset_index()
transposed_data.columns = ["Question", "Response"]
# transposed_data = transposed_data.drop(transposed_data.Question.isin(["Services","Department","service_url","Sector",	"nesda_parameter"]).index)
# transposed_data = transposed_data.notnull()
transposed_data = transposed_data[transposed_data["Response"].notnull()]
# df[~df['type'].isin(['hotel','Restaurant','estate'])]
st.write("Go to the service url to see more details")
st.write(transposed_data.loc[transposed_data["Question"]=="service_url","Response"])
transposed_data = transposed_data[~transposed_data['Question'].isin(["Services","Department","service_url","Sector","nesda_parameter"])]

st.dataframe(transposed_data, use_container_width=True)

df1 = transposed_data['Response'].value_counts().rename_axis('Assessment Response').reset_index(name='Counts')

st.write("Value Counts for NeSDA Parameters")
st.bar_chart(df1, x='Assessment Response', y='Counts', color='#00b3b3')



#st.caption("Please share feedback at siddharthsekhar_s@isb.edu")
