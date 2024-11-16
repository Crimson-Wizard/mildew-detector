import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
#from app_pages.page_summary import page_summary_body
from app_pages.page_findings import page_findings_body

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
#app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Findings", page_findings_body)


app.run()  # Run the app