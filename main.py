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
    st.title("CAGE Questionnaire for Alcohol Use")
    
    # Questions for the CAGE questionnaire
    questions = [
        "Have you ever felt you should Cut down on your drinking?",
        "Have people Annoyed you by criticizing your drinking?",
        "Have you ever felt bad or Guilty about your drinking?",
        "Have you ever had a drink first thing in the morning (Eye-opener) to steady your nerves or get rid of a hangover?"
    ]
    
    # Use checkboxes for questions
    responses = [st.checkbox(question) for question in questions]

    if st.button("Submit"):
        result = cage_questionnaire(responses)
        st.subheader("Results")
        st.write(result['interpretation'])

if __name__ == "__main__":
    main()
