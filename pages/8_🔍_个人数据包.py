
import streamlit as st
import zzfdemo.foliumap as zzfdemo

st.set_page_config(page_title="GEEMAP_Download_sl App",layout="wide"
)

col1, col2 = st.columns([4, 1])
Map = zzfdemo.Map()
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
    
    Map.to_streamlit(height=850)
