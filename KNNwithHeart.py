from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('การทำนายโรคหัวใจ❤️ด้วยเทคนิค Machine Learning')
st.image("./img/hog.jpg")
col1, col2, col3 = st.columns(3)

with col1:
   st.image("./img/rrr.jpg")

with col2:
   st.image("./img/yyy.jpg")

html_7 = """
<div style="background-color:#f7b3f1;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูล Heart3 หรือข้อมูลการเป็นโรคหัวใจสำหรับการทำนาย</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
st.markdown("")

st.subheader("ข้อมูลส่วนแรก 10 แถว")
dt = pd.read_csv("./data/Heart3.csv")
st.write(dt.head(10))
st.subheader("ข้อมูลส่วนสุดท้าย 10 แถว")
st.write(dt.tail(10))

# สถิติพื้นฐาน
st.subheader("📈 สถิติพื้นฐานของข้อมูล")
st.write(dt.describe())

# การเลือกแสดงกราฟตามฟีเจอร์
st.subheader("📌 เลือกฟีเจอร์เพื่อดูการกระจายข้อมูล")
feature = st.selectbox("เลือกฟีเจอร์", dt.columns[:-1])

# วาดกราฟ boxplot
st.write(f"### 🎯 Boxplot: {feature} แยกตามชนิดของดอกไม้")
fig, ax = plt.subplots()
sns.boxplot(data=dt, x='HeartDisease', y=feature, ax=ax)
st.pyplot(fig)

# วาด pairplot
if st.checkbox("แสดง Pairplot (ใช้เวลาประมวลผลเล็กน้อย)"):
    st.write("### 🌺 Pairplot:🐇การกระจายของข้อมูลทั้งหมด")
    fig2 = sns.pairplot(dt, hue='HeartDisease')
    st.pyplot(fig2)

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

A1 = st.number_input("กรุณาเลือกข้อมูล Age")
A2 = st.number_input("กรุณาเลือกข้อมูล Sex")
A3 = st.number_input("กรุณาเลือกข้อมูล ChestPainType")
A4 = st.number_input("กรุณาเลือกข้อมูล RestingBP")
A5 = st.number_input("กรุณาเลือกข้อมูล Cholesterol")
A6 = st.number_input("กรุณาเลือกข้อมูล FastingBS")
A7 = st.number_input("กรุณาเลือกข้อมูล RestingECG")
A8 = st.number_input("กรุณาเลือกข้อมูล MaxHR")
A9 = st.number_input("กรุณาเลือกข้อมูล ExerciseAngina")
A10 = st.number_input("กรุณาเลือกข้อมูล Oldpeak")
A11 = st.number_input("กรุณาเลือกข้อมูล ST_Slope")


if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/Heart3.csv") 
   X = dt.drop('HeartDisease', axis=1)
   y = dt.HeartDisease   

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)  
    
   x_input = np.array([[A1, A2,A3, A4,A5, A6,A7, A8,A9, A10,A11]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 'maipen':
    st.image("./img/ttt.jpg")
   elif out[0] == 'pen':       
    st.image("./img/eee.jpg")
else:
    st.write("ไม่ทำนาย")