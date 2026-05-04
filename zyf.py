import streamlit as st

st.title("🎂 Happy Birthday!")

st.image("birthday.jpg", caption="🎉 给你的生日祝福", use_container_width=True)

st.write("祝你生日快乐！")
st.write("希望你今天开心，天天开心！🎉")

if st.button("点我一下"):
    st.balloons()
    st.success("生日快乐！愿你越来越好！🎁")