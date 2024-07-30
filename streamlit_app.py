import os
import streamlit as st
from run_pipeline import run_pipeline

# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="FOA Information Extraction Generator", page_icon="img_banner.png",)
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -4rem;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # lightmode
# Design change height of text input fields headers
st.markdown('''<style>.css-qrbaxs {min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design change spinner color to primary color
st.markdown('''<style>.stSpinner > div > div {border-top-color: #9d03fc;}</style>''',
    unsafe_allow_html=True)
# Design change min height of text input box
st.markdown('''<style>.css-15tx938{min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design hide top header line
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def main_gpt3emailgen():

    st.image('img_banner.png')  # TITLE and Creator information
    st.markdown('Automatically extract important FOA Information')
    st.write('\n')  # add spacing
    
    count = 0
    st.subheader('\nWhat is the url link to the FOA you want to analyze?\n')
    with st.expander("FOA URL input", expanded=True):
        output_list = []
        input_c1 = st.text_input('Enter url(s) in the box. If multiple urls, delimit with a comma', 'url')
        if input_c1 != '':
            input_c1 = [i.strip() for i in input_c1.split(',')]
            if st.button('Generate Report'):
                st.write("Running extraction, please wait...") 
                for url in input_c1:
                    foa_title, foa_report = run_pipeline(url)
                    output_list.append((foa_title, foa_report))
                count += 1
    if count > 0:
        st.subheader('\nFOA Extraction Reports\n')
        for output in output_list:
            foa_title_output, foa_report_output = output[0], output[1]
            with st.expander(f"{foa_title_output} - Report", expanded=True):
                st.markdown(foa_report_output)  #output the results
               
                
if __name__ == '__main__':
    # call main function
    main_gpt3emailgen()
