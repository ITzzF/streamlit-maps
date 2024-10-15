import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/ITzzF/streamlit-maps>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "./data/1.gif"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "./data/us_cities.csv"
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="pop_max",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
