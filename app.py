import streamlit as st
from groq import Groq

# 1. إعداد الصفحة وتنسيق الخطوط والاتجاه (من اليمين لليسار)
st.set_page_config(page_title="مساعد اليوتيوبر الذكي", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    /* تنسيق مربعات الإدخال والنصوص */
    div[data-testid="stMarkdownContainer"] > p, h1, h2, h3 {
        text-align: right;
        direction: rtl;
    }
    input, textarea {
        direction: rtl !important;
        text-align: right !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 مساعد اليوتيوبر الذكي")
st.subheader("اصنع سكريبت فيديو احترافي في ثوانٍ")

# 2. ضع مفتاحك هنا (تأكد أنه يبدأ بـ gsk_ ولا يوجد قبله أو بعده مسافات)
api_key = "ضع_مفتاحك_هنا" 

client = Groq(api_key=api_key)

# 3. واجهة المستخدم
topic = st.text_input("ما هو موضوع الفيديو؟", placeholder="مثلاً: قصة كفاح ميسي...")
style = st.selectbox("أسلوب الكتابة", ["حماسي ومحفز", "تعليمي هادئ", "قصصي درامي"])

if st.button("توليد السكريبت ✨"):
    if topic:
        with st.spinner('جاري كتابة السكريبت بذكاء...'):
            try:
                # استخدام الموديل الأحدث llama-3.3-70b-versatile
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "أنت كاتب محتوى يوتيوب محترف. اكتب دائماً باللغة العربية. استخدم العناوين العريضة والنقاط لتنظيم السكريبت بشكل جميل."},
                        {"role": "user", "content": f"اكتب سكريبت يوتيوب بأسلوب {style} عن: {topic}"}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                
                # عرض النتيجة (تم تصحيح الوصول للبيانات هنا)
                script_text = chat_completion.choices[0].message.content
                st.success("تم التوليد بنجاح!")
                st.markdown("---")
                st.markdown(script_text)
                
            except Exception as e:
                st.error(f"حدث خطأ تقني: {e}")
    else:
        st.warning("رجاءً اكتب موضوع الفيديو أولاً")
