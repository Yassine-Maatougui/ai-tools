import streamlit as st
from groq import Groq

# عنوان التطبيق
st.title("🚀 مساعد اليوتيوبر الذكي")
st.subheader("اصنع سكريبت فيديو احترافي في ثوانٍ")

# ضع مفتاحك هنا بدلاً من الكلمة التوضيحية
api_key = "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" 

client = Groq(api_key=api_key)

# مدخلات المستخدم
topic = st.text_input("ما هو موضوع الفيديو؟", placeholder="مثلاً: أفضل 5 جوالات في 2024")
style = st.selectbox("أسلوب الكتابة", ["حماسي", "تعليمي هادئ", "كوميدي ساخر"])

if st.button("توليد السكريبت ✨"):
    if topic:
        with st.spinner('جاري كتابة السكريبت...'):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": f"أنت كاتب سكريبت يوتيوب محترف. اكتب سكريبت بأسلوب {style} باللغة العربية يتضمن مقدمة جذابة، محتوى مقسم لفقرات، وخاتمة تدعو للاشتراك."},
                        {"role": "user", "content": f"اكتب سكريبت عن: {topic}"}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                st.success("تم تجهيز السكريبت!")
                # هذا هو السطر الذي تم تصحيحه باضافة [0]
                st.write(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("رجاءً اكتب موضوع الفيديو أولاً")
