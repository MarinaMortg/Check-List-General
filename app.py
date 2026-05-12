import streamlit as st
 
st.title("*General English Checklist*")
 
#Answers#
st.subheader("Understanding/Comprehension")
understanding_answer = st.radio(
   "",
    ["переспрашивает, отвечает не по теме","теряется, понимает после повторения или переформулировки","понимает с первого раза, отвечает по сути"], 
    index = 1 
)
 
 
st.subheader("Fluency&Tempo of Speech")
fluency_tempo_answer = st.radio(
    "",
    ["длинные частые паузы", "есть паузы, речь медленная, но связная", "комфортный темп, речь плавная"],
    index = 1 
)
 
st.subheader("Confidence")
confidence_answer = st.radio(
    "", 
    ["боится говорить","теряется при ошибках/может перейти на русский", "продолжает говорить, сам/а исправляется"],
    index = 1 
)
 
st.subheader("Pronunciation/Intelligibility")
pronunciation_answer = st.radio(
    "",
    ["часто непонятно, мешает пониманию","в целом понятно","легко понятно"],
   index = 1
)
 
st.subheader("Coherence/Structure of Answers")
coherence_answer = st.radio(
    "",
    ["фразы обрывочные, нет логики", "слабая структура, перескакивает, но мысль понятна","лоигчно и последовательно"],
index = 1 
)
st.subheader("Grammar Accuracy")
grammar_answer = st.radio(
    "",
    ["ошибок много, мешают пониманию","ошибки есть, но не являются значительными", "редкие, незначительные ошибки/ошибок нет"],
)