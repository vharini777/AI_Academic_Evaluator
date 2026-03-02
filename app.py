import streamlit as st
import json
from llm_engine import evaluate_with_llm
from essay_engine import grammar_score, readability_score

st.title("AI Essay Evaluator")

essay = st.text_area("Paste Essay Here")

if st.button("Evaluate"):

    if essay.strip() == "":
        st.warning("Essay is empty.")
    else:
        with st.spinner("Evaluating..."):

            llm_output = evaluate_with_llm(essay)

            try:
                scores = json.loads(llm_output)

                thesis = scores.get("thesis", 0)
                argument = scores.get("argument", 0)
                organization = scores.get("organization", 0)
                coherence = scores.get("coherence", 0)

                grammar = grammar_score(essay)
                readability = readability_score(essay)

                final_score = (
                    thesis +
                    argument +
                    organization +
                    coherence +
                    grammar +
                    readability
                )

                st.subheader("Score Breakdown")
                st.write("Thesis:", thesis)
                st.write("Argument:", argument)
                st.write("Organization:", organization)
                st.write("Coherence:", coherence)
                st.write("Grammar:", grammar)
                st.write("Readability:", readability)

                st.subheader("Final Score")
                st.write(final_score)

                st.subheader("Feedback")
                st.write(scores.get("feedback", "No feedback generated."))

            except:
                st.error("Model did not return valid JSON.")