import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('attribution_studies.csv', dtype={
        'event_name': 'string',
        'event_period': 'string', 
        'event_year': 'string',
        'study_focus': 'string',
        'iso_country_code': 'string',
        'cb_region': 'string',
        'event_type': 'string',
        'classification': 'string',
        'summary_statement': 'string',
        'publication_year': 'int64',
        'citation': 'string',
        'source': 'string',
        'rapid_study': 'string',
        'link': 'string'
    })

def get_publication_year_list(df):
    return ['', 'All'] + sorted(df['publication_year'].unique().tolist())

def get_event_type_list(df):
    return ['', 'All'] + sorted(df['event_type'].unique().astype(str).tolist())

def get_cb_region_list(df):
    return ['', 'All'] + sorted(df['cb_region'].unique().astype(str).tolist())

data = load_data()

st.sidebar.title("Filters")

year = st.sidebar.selectbox(
    "Select Year", 
    get_publication_year_list(data), 
    key='year',
    index=0)  # Default to 'All'

# apply year filter
filtered_data = data.copy()
if year not in ['','All']:
    filtered_data = filtered_data[filtered_data['publication_year'] == year]

event_type = st.sidebar.selectbox(
    "Select Event Type", 
    get_event_type_list(filtered_data), 
    key='event_type',
    index=0)  # Default to 'All'

# apply event filter
if event_type not in ['','All']:
    filtered_data = filtered_data[filtered_data['event_type'] == event_type]

cb_region = st.sidebar.selectbox(
    "Select CB Region", 
    get_cb_region_list(filtered_data), 
    key='event_type',
    index=0)  # Default to 'All'

# apply cb_region filter
if cb_region not in ['','All']:
    filtered_data = filtered_data[filtered_data['cb_region'] == cb_region]

print(year, event_type, cb_region)