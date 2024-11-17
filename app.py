import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_findings import page_findings_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_ml_performance import page_ml_performance_body
from app_pages.page_project_summary import page_project_summary_body
# Create an instance of the app
app = MultiPage(app_name="Mildew Detector") 
# app pages
app.add_page("Project Summary", page_project_summary_body)
app.add_page("Findings", page_findings_body)
app.add_page("Hypothesis", page_hypothesis_body)
app.add_page("Mildew Detector", page_mildew_detector_body)
app.add_page("ML Performance", page_ml_performance_body)

# Run the app
app.run()