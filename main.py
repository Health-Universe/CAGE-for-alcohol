import streamlit as st

def cage_questionnaire(responses):
    # Calculate the score based on responses
    score = sum(responses)
    result = {
        'score': score,
        'interpretation': ''
    }
    
    # Interpret the score
    if score > 0:
        result['interpretation'] += f"You answered 'yes' to {score} out of 4 questions.\n"
        if score >= 2:
            result['interpretation'] += ("This might indicate a potential problem with alcohol use.\n"
                                         "Consider discussing your alcohol use with a healthcare professional.")
        else:
            result['interpretation'] += ("While a lower score suggests fewer issues, if you have any concerns "
                                         "about your drinking, it's wise to consult a professional.")
    else:
        result['interpretation'] = "You answered 'no' to all questions, which generally suggests a lower likelihood of alcohol use disorder."
    
    return result

def main():
    #st.title("CAGE Questionnaire for Alcohol Use", help="[LOINC: 72109-2]")
    st.markdown("<h1 style='font-size: 40px;'>CAGE Questionnaire for Alcohol Use</h1>", unsafe_allow_html=True, help="[LOINC: 72109-2]")
    with st.expander("About"):
        st.markdown("""
        [**Paper**](https://jamanetwork.com/journals/jama/article-abstract/394693) 📖 |
        [**Validation**](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(82)91579-3/fulltext) ✅
        """)
        
        st.markdown("This interactive web application provides a simple and confidential tool for individuals to screen for potential alcohol use disorders using the CAGE questionnaire. The CAGE questionnaire is a renowned, brief self-assessment tool that consists of four questions designed to identify behaviors associated with problematic drinking.")
    
    # Questions for the CAGE questionnaire
    questions = [
        "Have you ever felt you should Cut down on your drinking? [LOINC: 63616-7]",
        "Have people Annoyed you by criticizing your drinking? [LOINC: 76967-9]",
        "Have you ever felt bad or Guilty about your drinking? [LOINC: 97737-1]",
        "Have you ever had a drink first thing in the morning (Eye-opener) to steady your nerves or get rid of a hangover? [LOINC: 97736-3]"
    ]
    
    # Use checkboxes for questions
    responses = [st.checkbox(question) for question in questions]

    if st.button("Submit"):
        st.divider()
        result = cage_questionnaire(responses)
        st.subheader("Results")
        st.write(result['interpretation'])
    
    st.divider()
    st.markdown("""App Created by [Health Universe](https://www.healthuniverse.com) 🚀""")
if __name__ == "__main__":
    main()
