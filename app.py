 # my_profile.py
import streamlit as st 
import pandas as pd 
st.title('자기소개') 
# 본인 정보 수정하기! 
st.write('## 기본 정보') 
st.write('**이름**: 이소윤') 
st.write('**학과**: 인공지능소프트웨어학과') 
st.write('**학년**: 3학년') 
st.write('---')  # 구분선 
st.write('## 이번 학기 시간표') 
schedule = pd.DataFrame({ 
'요일': ['월', '화', '수', '목', '금'], 
'2교시': ['-', '-', '-', '-', '빅데이터분석프로젝트'], 
'3교시': ['-', '인공지능캡스톤디자인', '-', '인공지능서비스프로젝트', '빅데이터분석프로젝트'], 
'4교시': ['-', '인공지능캡스톤디자인', '-', '인공지능서비스프로젝트', '빅데이터분석프로젝트'],
'5교시': ['-', '인공지능캡스톤디자인', '-', '인공지능서비스프로젝트', '빅데이터분석프로젝트']
}) 
st.write(schedule) 
st.write('---') 
st.write('## 관심 분야') 
st.write('- 머신러닝') 
st.write('- 빅데이터 분석') 
st.write('- 웹 개발') 
st.write('---') 
st.write('## 이번 학기 목표') 
goals = pd.DataFrame({ 
'목표': ['졸업작품 완성', '정보처리산업기사 자격증', '포트폴리오 완성'], 
'달성률': [5, 10, 5] 
}) 
st.write(goals) 
st.bar_chart(goals.set_index('목표'))