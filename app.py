import streamlit as st
from groq import Groq

# 1. إعداد واجهة احترافية تدعم العربية
st.set_page_config(page_title="مساعد اليوتيوبر", layout="centered")

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
st.write("اصنع محتوى احترافي في ثوانٍ")

# 2. ضع مفتاحك هنا (تأكد من مسح النص ووضع مفتاح gsk_ الحقيقي)
# بدلاً من وضع المفتاح يدوياً، نطلبه من الخزنة (Secrets)
api_key = st.secrets["GROQ_API_KEY"]
st.markdown("---")
st.subheader("💎 اشترك في الباقة الاحترافية")
st.write("احصل على استخدام غير محدود ودعم فني مباشر وتحديثات يومية للأدوات.")

# رابط واتساب الخاص بك (استبدل الرقم برقمك مع مفتاح الدولة)
whatsapp_link = "https://wa.me"

if st.button("تواصل معنا للاشتراك عبر واتساب 💬"):
    st.write(f"👉 [اضغط هنا للانتقال للواتساب]({whatsapp_link})")

try:
    client = Groq(api_key=api_key)
except:
    st.error("تأكد من وضع مفتاح الـ API بشكل صحيح")

# 3. واجهة الإدخال
topic = st.text_input("ما هو موضوع الفيديو؟")
style = st.selectbox("أسلوب الكلام", ["حماسي جداً", "تعليمي هادئ", "قصصي درامي"])

if st.button("توليد السكريبت ✨"):
    if topic and api_key != "ضع_مفتاحك_هنا":
        with st.spinner('جاري الكتابة...'):
            try:
                               chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system", 
                            "content": "أنت كاتب سكريبت محترف. اكتب باللغة العربية الفصحى فقط. ممنوع تماماً استخدام أي حروف لاتينية أو رموز غريبة داخل الكلمات العربية. اجعل النص متناسقاً ونظيفاً."
                        },
                        {
                            "role": "user", 
                            "content": f"اكتب سكريبت يوتيوب احترافي ومنظم عن: {topic} بأسلوب {style}"
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.6, # تقليل الدرجة لجعل النص أكثر دقة وأقل خطأً
                    max_tokens=2048,
                    top_p=1,
                    stop=None,
                    stream=False,
                )

                
                # التصحيح الأهم: إضافة [0] هنا
                script_result = chat_completion.choices[0].message.content
                
                st.success("تم التجهيز!")
                st.markdown("---")
                st.markdown(script_result)
                
            except Exception as e:
                st.error("حدث خطأ في الاتصال، حاول مرة أخرى")
    else:
        st.warning("تأكد من كتابة الموضوع ووضع مفتاح الـ API")
