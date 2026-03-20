import streamlit as st
from groq import Groq

# 1. إعداد واجهة احترافية تدعم العربية والخطوط
st.set_page_config(page_title="مساعد اليوتيوبر الذكي", layout="centered")

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
st.write("أدوات الذكاء الاصطناعي لصناع المحتوى المحترفين")

# 2. جلب المفتاح من الخزنة (Secrets)
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except Exception as e:
    st.error("خطأ: تأكد من إضافة GROQ_API_KEY في إعدادات Secrets في Streamlit")
    st.stop()

# 3. واجهة إدخال البيانات
topic = st.text_input("ما هو موضوع الفيديو؟", placeholder="مثلاً: قصة نجاح إيلون ماسك")
style = st.selectbox("أسلوب الكلام", ["حماسي جداً", "تعليمي هادئ", "قصصي درامي"])

if st.button("توليد السكريبت ✨"):
    if topic:
        with st.spinner('جاري التأليف بذكاء...'):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system", 
                            "content": "أنت كاتب سكريبت محترف. اكتب باللغة العربية الفصحى فقط. ممنوع تماماً استخدام أي حروف لاتينية أو رموز غريبة داخل الكلمات العربية. نسق النص بعناوين واضحة ونقاط."
                        },
                        {
                            "role": "user", 
                            "content": f"اكتب سكريبت يوتيوب احترافي ومنظم عن: {topic} بأسلوب {style}"
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.6,
                )

                # استخراج النتيجة بشكل صحيح
                script_result = chat_completion.choices[0].message.content
                
                st.success("تم التجهيز بنجاح!")
                st.markdown("---")
                st.markdown(script_result)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء التوليد، يرجى المحاولة لاحقاً")
    else:
        st.warning("رجاءً اكتب موضوع الفيديو أولاً")

# 4. قسم الاشتراك (في أسفل الصفحة ليكون احترافياً)
st.markdown("---")
st.subheader("💎 باقة المحترفين (Premium)")
st.write("استخدام غير محدود، أفكار فيديوهات حصرية، ودعم فني مباشر.")

# ضع رقمك هنا بدلاً من الـ X (مثال: 966500000000)
whatsapp_number = "966XXXXXXXXX" 
whatsapp_link = f"https://wa.me{whatsapp_number}?text=أريد_الاشتراك_في_باقة_اليوتيوبر"

if st.button("تواصل للاشتراك عبر واتساب 💬"):
    st.markdown(f'<a href="{whatsapp_link}" target="_blank">👉 اضغط هنا لفتح المحادثة والاشتراك</a>', unsafe_allow_html=True)
