import streamlit as st
import pandas as pd
from PIL import Image

# 데이터 저장을 위한 데이터프레임 초기화
if 'trips' not in st.session_state:
    st.session_state.trips = pd.DataFrame(columns=['Destination', 'Start Date', 'End Date', 'Purpose', 'Notes', 'Travelers', 'Feelings', 'Image'])

# 앱 제목
st.title("여행 기록 앱")

# 여행 추가 함수
def add_trip(destination, start_date, end_date, purpose, notes, travelers, feelings, image):
    img = Image.open(image)
    new_trip = {
        'Destination': destination,
        'Start Date': start_date,
        'End Date': end_date,
        'Purpose': purpose,
        'Notes': notes,
        'Travelers': travelers,
        'Feelings': feelings,
        'Image': img
    }
    st.session_state.trips = st.session_state.trips.append(new_trip, ignore_index=True)

# 여행 삭제 함수
def delete_trip(index):
    st.session_state.trips = st.session_state.trips.drop(index).reset_index(drop=True)

# 여행 추가 입력 양식
st.subheader("여행 추가")
with st.form(key='add_trip_form'):
    destination = st.text_input("여행지")
    start_date = st.date_input("시작 날짜")
    end_date = st.date_input("종료 날짜")
    purpose = st.text_input("여행 목적")
    notes = st.text_area("메모", height=100)
    travelers = st.text_area("여행 동행자", height=100)  # 동행자 입력 필드 추가
    feelings = st.text_area("여행에서 느낀 점", height=100)  # 여행 느낀 점 입력 필드
    image = st.file_uploader("여행지 사진 업로드", type=["jpg", "jpeg", "png"])  # 사진 업로드 필드
    submit_button = st.form_submit_button(label='여행 추가')

    if submit_button:
        if image is not None:
            add_trip(destination, start_date, end_date, purpose, notes, travelers, feelings, image)
            st.success("여행이 추가되었습니다!")
        else:
            st.warning("이미지를 업로드해 주세요.")

# 여행 삭제 기능
st.subheader("여행 삭제")
if not st.session_state.trips.empty:
    delete_index = st.selectbox("삭제할 여행 선택", st.session_state.trips.index)
    if st.button("여행 삭제"):
        delete_trip(delete_index)
        st.success("여행이 삭제되었습니다!")

# 여행 목록 테이블
st.subheader("내 여행 기록")
if st.session_state.trips.empty:
    st.write("추가된 여행이 없습니다.")
else:
    for index, row in st.session_state.trips.iterrows():
        st.write(f"### 여행지: {row['Destination']}")
        st.write(f"**시작 날짜:** {row['Start Date']}")
        st.write(f"**종료 날짜:** {row['End Date']}")
        st.write(f"**여행 목적:** {row['Purpose']}")
        st.write(f"**메모:** {row['Notes']}")
        st.write(f"**여행 동행자:** {row['Travelers']}")  # 동행자 표시
        st.write(f"**여행에서 느낀 점:** {row['Feelings']}")  # 여행 느낀 점 표시
        if row['Image'] is not None:
            st.image(row['Image'], caption='여행지 사진', use_column_width=True)
        st.write("")  # 여백 추가
        import streamlit as st
import pandas as pd
from PIL import Image

# 데이터 저장을 위한 데이터프레임 초기화
if 'trips' not in st.session_state:
    st.session_state.trips = pd.DataFrame(columns=['Destination', 'Start Date', 'End Date', 'Purpose', 'Notes', 'Travelers', 'Feelings', 'Image'])

# 앱 제목
st.title("여행 기록 앱")

# 여행 추가 함수
def add_trip(destination, start_date, end_date, purpose, notes, travelers, feelings, image):
    img = Image.open(image)
    new_trip = {
        'Destination': destination,
        'Start Date': start_date,
        'End Date': end_date,
        'Purpose': purpose,
        'Notes': notes,
        'Travelers': travelers,
        'Feelings': feelings,
        'Image': img
    }
    st.session_state.trips = st.session_state.trips.append(new_trip, ignore_index=True)

# 여행 삭제 함수
def delete_trip(index):
    st.session_state.trips = st.session_state.trips.drop(index).reset_index(drop=True)

# 여행 추가 입력 양식
st.subheader("여행 추가")
with st.form(key='add_trip_form'):
    destination = st.text_input("여행지")
    start_date = st.date_input("시작 날짜")
    end_date = st.date_input("종료 날짜")
    purpose = st.text_input("여행 목적")
    notes = st.text_area("메모", height=100)
    travelers = st.text_area("여행 동행자", height=100)  # 동행자 입력 필드 추가
    feelings = st.text_area("여행에서 느낀 점", height=100)  # 여행 느낀 점 입력 필드
    image = st.file_uploader("여행지 사진 업로드", type=["jpg", "jpeg", "png"])  # 사진 업로드 필드

    submit_button = st.form_submit_button(label='여행 추가')

    if submit_button:
        if image is not None:
            add_trip(destination, start_date, end_date, purpose, notes, travelers, feelings, image)
            st.success("여행이 추가되었습니다!")
            st.image(image, caption='업로드된 여행지 사진', use_column_width=True)  # 사진을 업로드 후 바로 보여줌
        else:
            st.warning("이미지를 업로드해 주세요.")

# 여행 삭제 기능
st.subheader("여행 삭제")
if not st.session_state.trips.empty:
    delete_index = st.selectbox("삭제할 여행 선택", st.session_state.trips.index)
    if st.button("여행 삭제"):
        delete_trip(delete_index)
        st.success("여행이 삭제되었습니다!")

# 여행 목록 테이블
st.subheader("내 여행 기록")
if st.session_state.trips.empty:
    st.write("추가된 여행이 없습니다.")
else:
    for index, row in st.session_state.trips.iterrows():
        st.write(f"### 여행지: {row['Destination']}")
        st.write(f"**시작 날짜:** {row['Start Date']}")
        st.write(f"**종료 날짜:** {row['End Date']}")
        st.write(f"**여행 목적:** {row['Purpose']}")
        st.write(f"**메모:** {row['Notes']}")
        st.write(f"**여행 동행자:** {row['Travelers']}")  # 동행자 표시
        st.write(f"**여행에서 느낀 점:** {row['Feelings']}")  # 여행 느낀 점 표시
        if row['Image'] is not None:
            st.image(row['Image'], caption='여행지 사진', use_column_width=True)  # 저장된 이미지 표시
        st.write("")  # 여백 추가