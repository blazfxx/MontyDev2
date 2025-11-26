"""
Utility helpers for the Streamlit app.

`safe_rerun()` provides a compatibility wrapper around Streamlit's
reload/rerun functionality that works across different versions.
"""
import time
import streamlit as st


def safe_rerun():
    """Try multiple rerun strategies across streamlit versions.

    - Preferred: st.experimental_rerun()
        - Fallback: change query params by setting `st.query_params` (replaces
            the soon-to-be-deprecated `st.experimental_set_query_params`).
    - Final fallback: st.stop() to ensure any session updates are flushed and
      the current run exits; user can then navigate to another page.
    """
    try:
        # Supported on many streamlit versions
        st.experimental_rerun()
        return
    except Exception:
        pass

    try:
        # Changing query params using the supported `st.query_params` setter
        # forces a rerun in many contexts. Use a copy to avoid mutating
        # the object in-place if it's read-only in this Streamlit version.
        params = dict(st.query_params) if hasattr(st, 'query_params') else {}
        params['_rerun'] = int(time.time())
        st.query_params = params
        return
    except Exception:
        pass

    # Last-resort: stop the script and rely on user actions to re-render.
    try:
        st.stop()
    except Exception:
        # If even stop isn't available, give up silently.
        return
