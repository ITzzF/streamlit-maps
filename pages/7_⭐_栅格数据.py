import ee
import streamlit as st
import geemap.foliumap as geemap

# geemap.set_proxy(port=7897)
@st.cache_data
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)
st.set_page_config(page_title="GEEMAP_Download_sl App",layout="wide"
)

col1, col2 = st.columns([4, 1])

# with col2:
    # ROI = st.text_input('The google earth engine roi geometry', 'users/yamiletsharon250/wuhan')
    # count = st.number_input("How many image chips to export", 1000)
    # buffer = st.number_input("The buffer distance (m) around each point", 2560)
    # scale = st.number_input("The scale to do stratified sampling", 10)
    # dimensions = st.text_input("The scale to do stratified sampling",'256x256')
    # prefix = st.text_input('The filename prefix', 'tile_')
    # processes = st.number_input('How many processes to used for', 25)
    # label_out_dir = st.text_input('The label output directory', '/label')
    # val_out_dir = st.text_input('The val output directory', '/val')
    # format = st.selectbox(
    # 'The output image format',
    # ('png', 'jpg', 'ZIPPED_GEO_TIFF', 'GEO_TIFF', 'NPY'))


with col1:
    ee_authenticate(token_name="EARTHENGINE_TOKEN")
    Map = geemap.Map()
    in_geojson = "./data/china.geojson"
    vector  = geemap.geojson_to_ee(in_geojson)
    roi = vector.filter(ee.Filter.eq('name', '河南省'))
    Map.addLayer(roi,{},'河南省')
    collection = (
    ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
    .filterDate('2024-01-01', '2024-10-01')
    .filterBounds(roi)
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
    
    )
    image = collection.median()

    vis = {
        'min': 0.0,
        'max': 3000,
        'bands': ['B4', 'B3', 'B2'],
    }
    Map.addLayer(image.clip(roi), vis, 'Sentinel-2')
    Map.to_streamlit(height=850)
