import streamlit as st

st.set_page_config(
    page_title="Universities Information",
    page_icon="👋",
)

st.title("Homepage")
#st.sidebar.success("Select a page above.")

# Introduction to corpus
st.write("""
### Introduction to Corpus

Our project aims to annotate university information according to various parameters including City Size, Type of Institution, Year of Insitution's History, Economic Development Level, and Country Develop Level. The annotation plan includes the following criteria:
- **City Size:** Extra Large, Large, Middle, or Small cities based on the population size of the metropolitan area.
- **Type of Institution:** Public or Private.
- **Year of Insitution's History:** Historic, Old or Young.
- **Economic Development Level:** Very High Income, High Income, Medium Income or low Income based on GDP per Capita(US$).
- **Country Develop Level:** Developed or developing.

Annotators will be the 4 members in our team, ensuring inter-annotator agreement through cross-annotated records. Quality assurance steps include training sessions and pilot studies.

""")

st.write("""
### Access to Corpus and Annotations

Users can access to the corpus and annotations data using the search functions by clicking the pages on the left.
- **Search by Name** : Input the name of the university to retrieve introduction of this university (the corpus text).
- **Search by Filter** : Retrieve relevant university data by using filtering indicators (annotated tags).
- **Search for Similar Universities** : Input the name of the university to retrieve universities with the same annotated tags.
         
         
""")
