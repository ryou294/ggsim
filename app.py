import streamlit as st
import random

def tenjou():
    st.text("★★★★★ セノ")
    st.session_state.count = 0


def karitenjou():
    c = random.randint(1,2)
    if c == 1:
        st.text("★★★★★ セノ")
        st.session_state.count = 0
    else:
        a = random.randint(1,6)
        if a == 1:
            st.text("★★★★★ ジン")
        elif a == 2:
            st.text("★★★★★ ディルック")
        elif a == 3:
            st.text("★★★★★ モナ")
        elif a == 4:
            st.text("★★★★★ 刻晴")
        elif a == 5:
            st.text("★★★★★ 七七")
        elif a == 6:
            st.text("★★★★★ ティナリ")

def hosyou():
    n = random.randint(1,1000)
    if n <= 6:
        m = random.randint(1,2)
        if m == 1:
            st.text("★★★★★ セノ")
            st.session_state.count = 0
        else:
            p = random.randint(1,6)
            if p == 1:
                st.text("★★★★★ ジン")
            elif p == 2:
                st.text("★★★★★ ディルック")
            elif p == 3:
                st.text("★★★★★ モナ")
            elif p == 4:
                st.text("★★★★★ 刻晴")
            elif p == 5:
                st.text("★★★★★ 七七")
            elif p == 6:
                st.text("★★★★★ ティナリ")
    else:
        q = random.randint(1,2)
        if q == 1:
            b = random.randint(1,3)
            if b == 1:
                st.text("★★★★ コレイ")
            if b == 2:
                st.text("★★★★ ベネット")
            if b == 3:
                st.text("★★★★ バーバラ")
        else:
            st.text("★★★★")    

def gacha():
    n = random.randint(1,1000)
    if n <= 6:
        m = random.randint(1,2)
        if m == 1:
            st.text("★★★★★ セノ")
            st.session_state.count = 0
        else:
            p = random.randint(1,6)
            if p == 1:
                st.text("★★★★★ ジン")
            elif p == 2:
                st.text("★★★★★ ディルック")
            elif p == 3:
                st.text("★★★★★ モナ")
            elif p == 4:
                st.text("★★★★★ 刻晴")
            elif p == 5:
                st.text("★★★★★ 七七")
            elif p == 6:
                st.text("★★★★★ ティナリ")
    elif n <=57:
        q = random.randint(1,2)
        if q == 1:
            b = random.randint(1,3)
            if b == 1:
                st.text("★★★★ コレイ")
            if b == 2:
                st.text("★★★★ ベネット")
            if b == 3:
                st.text("★★★★ バーバラ")
        else:
            st.text("★★★★")
    else:
        st.text("★★★")

if 'count' not in st.session_state:
    st.session_state.count = 0

st.title("原神祈願シミュ")
st.caption("原神風のアプリです。")


#フォームの形成
with st.form(key="profile_form"):
    #テキストボックス
   

    #ボタン
    gacha_btn = st.form_submit_button("1回祈願")
    tyvat_btn = st.form_submit_button("10回祈願")
    
    if gacha_btn == True:
        gacha()

    if tyvat_btn ==True:
        st.session_state.count += 10
        st.text(str(st.session_state.count)+"連目")
        for i in range(10):
            if i != 9:
                gacha()
            else:
                if st.session_state.count == 80:
                    karitenjou()
                elif st.session_state.count == 160:
                    tenjou()
                else:
                    hosyou()