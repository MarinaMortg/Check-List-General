import streamlit as st

st.markdown("""
<style>
h3 {
    margin: 0 !important;
    padding: 0 !important;
}
 
div[role="radiogroup"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)
 
 
st.title("*General English Checklist*")

col1, spacer, col2 = st.columns([1, 0.3, 1])
""

#Answers#
with col1:
    st.markdown("<div style='padding-right: 20px'></div>", unsafe_allow_html=True)
``

   

    st.subheader("Understanding/Comprehension")
    
    
    understanding_answer = st.radio(
   "",
    ["переспрашивает, отвечает не по теме","теряется, понимает после повторения или переформулировки","понимает с первого раза, отвечает по сути"], 
    index = 1 
)
 
 
    st.subheader("Fluency/Tempo of Speech")
    fluency_tempo_answer = st.radio(
    "",
    ["длинные частые паузы", "есть паузы, речь медленная, но связная", "комфортный темп, речь плавная"],
    index = 1 
)
    st.subheader("Confidence")
    confidence_answer = st.radio(
    "", 
    ["боится говорить","теряется при ошибках/может перейти на русский", "продолжает говорить, сам исправляется"],
    index = 1 
)

with col2:
    st.markdown("<div style='padding-left: 20px'></div>", unsafe_allow_html=True)
``
    st.subheader("Pronunciation/Intelligibility")
    pronunciation_answer = st.radio(
    "",
    ["часто непонятно, мешает пониманию","в целом понятно","легко понятно"],
   index = 1
)
    st.subheader("Coherence/Structure of Answers")
    coherence_answer = st.radio(
    "",
    ["фразы обрывочные, нет логики", "слабая структура, перескакивает, но мысль понятна","логично и последовательно"],
index = 1 
)
    st.subheader("Grammar Accuracy")
    grammar_answer = st.radio(
    "",
    ["ошибок много, мешают пониманию","ошибки есть, но не являются значительными", "редкие и незначительные ошибки/ошибок нет"],
)
#Scores#
 
    Understanding_Scores = {
    "переспрашивает, отвечает не по теме": 0,
    "теряется, понимает после повторения или переформулировки": 1,
    "понимает с первого раза, отвечает по сути": 2,
}
    Fluency_Scores = {
    "длинные частые паузы":0,
    "есть паузы, речь медленная, но связная":1,
"комфортный темп, речь плавная": 2
}
Confidence_Scores = {
    "боится говорить":0,
    "теряется при ошибках/может перейти на русский":1,
    "продолжает говорить, сам исправляется":2,
    }
Pronunciation_Scores = {
    "часто непонятно, мешает пониманию":0,
    "в целом понятно":1,
    "легко понятно":2,
    }
Coherence_Scores = {
    "фразы обрывочные, нет логики":0,
    "слабая структура, перескакивает, но мысль понятна":1,
    "логично и последовательно":2,
}
Grammar_Scores = {
        "ошибок много, мешают пониманию":0,
    "ошибки есть, но не являются значительными":1,
"редкие и незначительные ошибки/ошибок нет":2,
    }
 
#Scores2#
total_score = (
    Understanding_Scores[understanding_answer] +
    Fluency_Scores[fluency_tempo_answer] +
    Confidence_Scores[confidence_answer]+
    Pronunciation_Scores[pronunciation_answer]+
    Coherence_Scores[coherence_answer]+
    Grammar_Scores[grammar_answer]
)

 
def get_result_by_score(score):
    if score < 3:
        return "❌ Not OK(A1-A2)"
    elif score <= 6:
        return "❌ Not OK(A2-B1)"
    elif score <=7:
        return "⚠️ Partially OK(B2)"
    else:
        return "✅ Excellent (С1)"
#Result#
if st.button("Показать результат"):
   result = get_result_by_score(total_score)
   st.success(result)
