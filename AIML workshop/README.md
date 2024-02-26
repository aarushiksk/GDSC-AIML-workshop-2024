Step 1: pip install -q -U google-generativeai


Step 2: pip install streamlit

Step 3: check if both are available or not using 'pip show google.generativeai streamlit'

# To comment code out: Use ctrl+ / after selecting



Step 3: streamlit basic
# Title of the app
st.title('Basic Streamlit App')

# Header
st.header('This is a header')

# Subheader
st.subheader('This is a subheader')

# Text
st.write('This is some text.')

# Markdown
st.markdown('**This** is markdown.')

# Button
if st.button('Click me!'):
    st.write('Button clicked!')

# Checkbox
checkbox_state = st.checkbox('Check me!')
if checkbox_state:
    st.write('Checkbox checked!')