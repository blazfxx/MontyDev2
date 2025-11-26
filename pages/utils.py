
import time
import streamlit as st


def safe_rerun():

    try:
        st.experimental_rerun()
        return
    except Exception:
        pass

    try:

        params = dict(st.query_params) if hasattr(st, 'query_params') else {}
        params['_rerun'] = int(time.time())
        st.query_params = params
        return
    except Exception:
        pass

    try:
        st.stop()
    except Exception:
        return
