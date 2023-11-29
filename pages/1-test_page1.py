import streamlit as st
import datetime as dt


if "duration" not in st.session_state:
    st.session_state.duration = None
start_time = st.time_input("enter a time",dt.time(hour=1,minute=00))
start_time = dt.timedelta(hours=start_time.hour,minutes=start_time.minute)


end_time = st.time_input("enter a time",dt.time(hour=2,minute=00))
end_time = dt.timedelta(hours=end_time.hour,minutes=end_time.minute)
duration = end_time - start_time
st.write("the duration between start time and end time is:",duration)

st.session_state["duration"] = duration

