import streamlit as st
from google_suggest import get_neutral_google_suggests

# Streamlitアプリケーションの設定
st.title('Google Suggest サジェスト取得アプリ')
query = st.text_input('検索クエリを入力してください:', '医師 結婚')

if st.button('サジェスト取得'):
    suggests = get_neutral_google_suggests(query, language='ja', region='jp')
    if suggests:
        st.write('サジェスト結果:')
        for i, suggest in enumerate(suggests):
            st.write(f"{i + 1}. {suggest}")
    else:
        st.write('サジェスト結果がありません。')
