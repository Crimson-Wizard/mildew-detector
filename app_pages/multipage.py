import streamlit as st


class MultiPage:
    """
    A class to manage multiple pages in a Streamlit app.
    This allows for modularization of the app into separate pages,
    each with its own title and functionality.
    """
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    # Add a new page to the application.
    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    # Run the MultiPage app
    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
