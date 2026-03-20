import streamlit as st
from groq import Groq

# إعداد واجهة الصفحة لتكون مريحة للعين وتدعم العربية
st.set_page_config(page_title="مساعد اليوتيوبر الذكي", layout="centered")

# إضافة تنسيق CSS لجعل النص من اليمين لليسار (RTL)
st.markdown("""
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    div[data-testid="stMarkdownContainer"] > p {
        text-align: right;
    }
    div[data-baseweb="select"] {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 مساعد اليوتيوبر الذكي")
st.subheader("اصنع سكريبت فيديو احترافي في ثوانٍ")

# تأكد من وضع مفتاحك الحقيقي هنا
api_key = "ضع_مفتاحك_هنا" 

client = Groq(api_key=api_key)

topic = st.text_input("ما هو موضوع الفيديو؟", placeholder="مثلاً: أفضل 5 جوالات في 2024")
style = st.selectbox("أسلوب الكتابة", ["حماسي", "تعليمي هادئ", "قصصي مشوق"])

if st.button("توليد السكريبت ✨"):
    if topic:
        with st.spinner('جاري كتابة السكريبت بذكاء...'):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "أنت كاتب سكريبت يوتيوب محترف. اكتب باللغة العربية الفصحى البسيطة والمنظمة جداً. استخدم عناوين واضحة ونقاط. اجعل النص يبدأ من اليمين."},
                        {"role": "user", "content": f"اكتب سكريبت {style} عن: {topic}"}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                st.success("تم تجهيز السكريبت بنجاح!")
                # عرض السكريبت داخل مربع نص مرتب
                st.markdown("---")
                st.markdown(f"### 📝 السكريبت المقترح:\n\n{chat_completion.choices[0].message.content}")
            except Exception as e:
                st.error(f"حدث خطأ تقني: {e}")
    else:
        st.warning("رجاءً اكتب موضوع الفيديو أولاً")
