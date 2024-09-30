import streamlit as st
import pandas as pd

#page config
st.set_page_config(
    page_title="Search by Name",
    page_icon="👋",
)
st.title("Search by Name")

# load dataframe
filename = 'final_annotation_clean.xlsx'
df = pd.read_excel(filename, header=0)
uni_lst = df['University Name'].unique().tolist()

#input name
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input the name of the university here", st.session_state["my_input"])

mask = df['University Name'].str.contains(my_input, case=False)

# submit function

def show(mask, df):
    df_filtered = df[mask]
    df_filtered_lst = df_filtered.to_dict('records')

    st.markdown(f'*Available Results: {df_filtered.shape[0]}*')

    for d in df_filtered_lst:
        st.write('-------------------------')

        col1, col2, col3 = st.columns([1, 5, 2])
        with col1:
            st.write(':sports_medal:', str(d['Ranking']))
        with col2:
            st.subheader(f"**{d['University Name']}**")
            st.write(d['Corpus Text'])
        with col3:
            st.write(':earth_americas: ', d["Country"])
            st.write(':school:', d['Type of Institution'])
            st.write(':hourglass_flowing_sand:', d["Year of Insitution's History"])
            st.write(':moneybag:', d['Economic Development Level'])
            st.write(':city_sunset:', d['City Size'], ' City Size')

submit = st.button("Submit")
if submit:
    show(mask, df)


    
        
