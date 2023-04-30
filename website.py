import pandas as pd
import numpy as np
import streamlit as st

# df = pd.read_csv("../data/Hospitals.csv")
# df.head()

st.title('Immunisation Nation')
st.subheader('cause we gotta get them all immunized at some point yo')

# Streamlit writing
st.text('Immunization is one of the most effective public health interventions\navailable, preventing millions of deaths each year from \nvaccine-preventable diseases such as measles, polio, tetanus, and \nhepatitis B. Immunizations are crucial for protecting individuals, \ncommunities, and entire populations from the spread of infectious \ndiseases.')

st.divider()

st.subheader('What are we trying to attain?')

st.text('We want to find out how a certain immunisation goal affects the number of \nresources we need to attain that goal')

st.image('https://images.unsplash.com/photo-1613758947307-f3b8f5d80711?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fHZhY2NpbmF0aW9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60')
st.text('Photo by Iván Díaz on Unsplash')
# Sliders + widget updating
x = st.slider("Slider", 10, 200, 15)


# pandas integration
df = pd.DataFrame({"Name": ['Darren'], "Age": ["21"]})
# st.write(df)
df

# charts
df = pd.DataFrame({"Age": np.random.randn(5)})

st.line_chart(df)


# checkbox


# sidebar
#st.sidebar.title("Made by Cornellians")

st.sidebar.write('Dan Wei Zuo, Alyssa Serebrenik, Andrea Siby, Arya Patel, Nicole Hao')
st.text("We got our datasets from OECD.Statistics at https://stats.oecd.org/BrandedView.aspx?oecd_bv_id=na-data-en&doi=data-00368-en# ")