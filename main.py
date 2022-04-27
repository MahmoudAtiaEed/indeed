from indeed.indeed import *
url = st.text_input("paste an indeed url")
b = st.button("see data frame")
if b:
    jop = indeed(url)

    st.table(jop.get_jops())
