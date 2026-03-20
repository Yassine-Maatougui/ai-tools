import streamlit as st
from groq import Groq

# إعداد واجهة الصفحة
st.set_page_config(page_title="مساعد اليوتيوبر الذكي", layout="centered")

# تنسيق اللغة العربية من اليمين لليسار
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    div[data-testid="stMarkdownContainer"] > p {
        text-align: right;
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 مساعد اليوتيوبر الذكي")
st.subheader("اصنع سكريبت فيديو احترافي في ثوانٍ")

# ضع مفتاحك الحقيقي هنا (تأكد من بقاء علامات التنصيص)
api_key = "ضع_مفتاحك_هنا" 

client = Groq(api_key=api_key)

topic = st.text_input("ما هو موضوع الفيديو؟", placeholder="اكتب فكرتك هنا...")
style = st.selectbox("أسلوب الكتابة", ["حماسي جداً", "تعليمي هادئ", "قصصي مشوق"])

if st.button("توليد السكريبت ✨"):
    if topic:
        with st.spinner('جاري التفكير والكتابة بالعربية...'):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "أنت كاتب محتوى يوتيوب محترف. اكتب دائماً باللغة العربية. نسّق النص باستخدام العناوين والنقاط بصيغة Markdown."},
                        {"role": "user", "content": f"اكتب سكريبت يوتيوب بأسلوب {style} عن: {topic}"}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                
                # الحصول على النص وتأمين عرضه
                result = chat_completion.choices[0].message.content
                st.success("تم تجهيز السكريبت بنجاح!")
                st.markdown("---")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"حدث خطأ: تأكد من مفتاح الـ API أو حاول مرة أخرى.")
    else:
        st.warning("رجاءً اكتب موضوع الفيديو أولاً")
