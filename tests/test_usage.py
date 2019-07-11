from pytest_dash.wait_for import (
    wait_for_text_to_equal,
    wait_for_element_by_css_selector
)

from pytest_dash.application_runners import import_app


# Basic test for the component rendering.
def test_render_component(dash_threaded):
    # Start a dash app contained in `usage.py`
    # dash_threaded is a fixture by pytest-dash
    # It will load a py file containing a Dash instance named `app`
    # and start it in a thread.
    driver = dash_threaded.driver
    app = import_app('usage')
    dash_threaded(app)

    #TODO: write test to check that script was indeed loaded ...
