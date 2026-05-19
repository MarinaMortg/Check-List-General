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


#Answers#
with col1:
    st.markdown("<div style='padding-right: 20px'></div>", unsafe_allow_html=True)

    st.subheader("Understanding/Comprehension")
    understanding_answer = st.radio(
   "",
    ["понимает неверно/отвечает не по теме","понимает после повторения или переформулировки","понимает с первого раза, отвечает по сути"], 
    index = 1 
)
    st.subheader("Fluency/Tempo of Speech")
    fluency_tempo_answer = st.radio(
    "",
    ["речь прерывистая: частые паузы, сложно формулировать мысль", "речь связная, но замедленная, есть заметные паузы", "комфортный темп, речь плавная"],
    index = 1 
)
    st.subheader("Confidence")
    confidence_answer = st.radio(
    "", 
    ["избегает говорить, отвечает минимально/неуверенно","говорит, но теряется при сложностях/может сбиваться или перейти на русский", "не теряется, сам исправляется"],
    index = 1 
)

with col2:
    st.markdown("<div style='padding-left: 20px'></div>", unsafe_allow_html=True)
    st.subheader("Coherence/Structure of Answers")
    coherence_answer = st.radio(
    "",
    ["нет логики, сложно понять мысль", "логика есть, но структура слабая","логично и структурировано"],
index = 1 
)
    st.subheader("Grammar Accuracy")
    grammar_answer = st.radio(
    "",
    ["ошибок много, мешают пониманию","ошибки есть, но не являются значительными", "редкие и незначительные ошибки/ошибок нет"],
)
    st.subheader("Pronunciaton/Speech Clarity")
    pronunciation_speechclarity_answer = st.radio(
        "",
        ["сильный акцент","заметный акцент, но в простом общении допустим", "легкий/нейтральный акцент"],
        index = 1
)
#Scores#
 
    Understanding_Scores = {
    "понимает неверно/отвечает не по теме": 0,
    "понимает после повторения или переформулировки": 1,
    "понимает с первого раза, отвечает по сути": 2,
}
    Fluency_Scores = {
    "речь прерывистая: частые паузы, сложно формулировать мысль":0,
    "речь связная, но замедленная, есть заметные паузы":1,
     "комфортный темп, речь плавная": 2
}
Confidence_Scores = {
    "избегает говорить, отвечает минимально/неуверенно":0,
    "говорит, но теряется при сложностях/может сбиваться или перейти на русский":1,
    "продолжает говорить, сам исправляется":2,
    }
Coherence_Scores = {
    "нет логики, сложно понять мысль":0,
    "логика есть, но структура слабая":1,
    "логично и структурировано":2,
}
Grammar_Scores = {
        "ошибок много, мешают пониманию":0,
    "ошибки есть, но не являются значительными":1,
"редкие и незначительные ошибки/ошибок нет":2,
}
    
Pronunciation_Speechclarity_Scores ={
    "сильный акцент":0,
    "заметный акцент, но в простом общении допустим":1,
    "легкий/нейтральный акцент":2,
}


#Scores2#
total_score = (
    Understanding_Scores[understanding_answer] +
    Fluency_Scores[fluency_tempo_answer] +
    Confidence_Scores[confidence_answer]+
    Coherence_Scores[coherence_answer]+
    Grammar_Scores[grammar_answer]+
    Pronunciation_Speechclarity_Scores[pronunciation/speechclarity_answer]
)

 
def get_result_by_score(score):
    if score < 3:
        return "❌ Not OK(A1-A2)"
    elif score <= 6:
        return "❌ Not OK(A2-B1)"
    elif score <=10:
        return "⚠️ Partially OK(B2)"
    else:
        return "✅ Excellent (С1)"
#Result#
if st.button("Показать результат"):
   result = get_result_by_score(total_score)
   st.success(result)
