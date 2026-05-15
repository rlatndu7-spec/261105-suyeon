import streamlit as st

st.set_page_config(
    page_title="자기소개 페이지",
    page_icon="👋",
    layout="centered",
)

st.title("👋 안녕하세요!")
st.subheader("간단한 자기소개 페이지에 오신 것을 환영합니다.")

st.markdown("---")

st.header("소개")
st.write(
    "안녕하세요! 저는 여기서 차차 내용을 채워갈 예정입니다. 이 페이지는 기본적인 자기소개 형식으로 구성되어 있으며, 추후에 프로젝트, 관심사, 연락처 등을 추가할 수 있습니다.\n"
    "안녕하세요! 김수연입니다. 어제 11시에 잠들었고 오늘 9시에 일어났어요~"
)

st.header("기본 정보")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**이름**")
    st.write("김수연")
    st.markdown("**학교**")
    st.write("청주교대")
    st.markdown("**나이**")
    st.write("23세")
with col2:
    st.markdown("**관심 분야**")
    st.write("영어교육, 웰빙")
    st.markdown("**학습 중인 기술**")
    st.write("Python, Streamlit, 머신러닝")

st.markdown("---")

st.header("TMI")
st.write("안녕하세요, 저는 김수연입니다. 현재 청주교대에 재학 중이며, 이 페이지는 제 자기소개를 보여주는 공간입니다.")

st.markdown(
    "- **요즘 걱정거리**: 몸이 잘 붓고, 당과 지방을 적게 섭취해야 하는데 쉽지 않아요.\n"
    "- **원하는 것**: 많이 먹어도 살찌지 않는 몸이 되는 것, 그리고 종강하기.\n"
    "- **주말 계획**: 엄마가 자취방에 놀러 오고, 드디어 에어컨 청소 회사 사람들이 온다!\n"
    "- **스스로에 대한 다짐**: 영어공부를 더 성실하게 열심히 하자. 영어 잘하고 싶잖아!"
)
