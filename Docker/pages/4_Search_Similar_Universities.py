import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Search for Similar Universities",
    page_icon="👋",
)
st.title("Search for Similar Universities")


# load dataframe
filename = 'final_annotation_clean.xlsx'
df = pd.read_excel(filename, header=0)

# list
ranking_lst = df['Ranking'].unique().tolist()
uni_lst = df['University Name'].unique().tolist()
country_lst = df['Country'].sort_values().unique().tolist()
citysize_lst = ['Small', 'Medium', 'Large', 'Extra Large']
type_lst = ['Public', 'Private']
year_lst = ['Historic', 'Old', 'Young']
econ_lst = ['Low Income', 'Medium Income', 'High Income', 'Very High Income']
dev_lst = ['Developed', 'Developing']


# filters

def filter_selection(name, lst, type, default=None):
    selection_lst = lst
    toggle_button = st.toggle(name)
    if toggle_button:
        if type == 'multiselect':
            selection = st.multiselect('', lst, label_visibility="collapsed")
            selection_lst = list(selection)
        elif type == 'selectbox':
            selection = st.selectbox('', (lst), label_visibility="collapsed")
            selection_lst = [selection]
        elif type =='radio':
            selection = st.radio('', lst, horizontal=True, label_visibility="collapsed")
            selection_lst = [selection]
    
    return selection_lst


uni = st.selectbox('', (uni_lst), label_visibility="collapsed", index=None, placeholder='Choose or input the name of university')


uni_df = df[df['University Name'].isin([uni])]
citysize = uni_df['City Size']
country = uni_df['Country']
type = uni_df['Type of Institution']
year = uni_df["Year of Insitution's History"]
econ = uni_df["Economic Development Level"]

mask = (
        (df['City Size'].isin(citysize)) 
        & (df['Country'].isin(country))
        & (df['Type of Institution']).isin(type)
        & (df["Year of Insitution's History"]).isin(year)
        & (df["Economic Development Level"]).isin(econ)
    )


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
