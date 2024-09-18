import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
#import plotly.graph_objects as go

st.title('Download button')

# Use st.cache_data instead of st.cache
@st.cache_data
def data_read(data):
    return data.to_csv().encode('utf-8')

# Read CSV file
data = pd.read_csv(r"C:\Users\DELL\Documents\player.csv")

# Generate CSV for download
csv = data_read(data)

# Corrected label spelling
st.download_button(
    label='Download CSV',
    data=csv,
    file_name='player.csv',
    mime='text/csv'
)


with open(r'C:\Users\DELL\Pictures\360.jpg','rb') as file:
  st.download_button(
  label='download image',
 data = file,
 file_name='img.png',
 mime='image/png'
 )

