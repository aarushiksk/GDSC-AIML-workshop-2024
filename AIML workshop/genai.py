import  google.generativeai as genai
import streamlit as st
genai.configure(api_key="YOUR_API_KEY_HERE")

model= genai.GenerativeModel('gemini-pro')
chat= model.start_chat(history=[])

# paragraph=input("Enter paragraph here:")
# response= chat.send_message("Summarise the paragraph for the user"+paragraph)
# print(response.text)


def main():
 st.title("text summarization app")
 
 paragraph=st.text_area("Enter your paragraph here:","")
 
 if paragraph: 
     
     if st.button("Summarize"):
         
        summary_text= chat.send_message("Summarise the paragraph in 50 words:"+paragraph)
        
        st.subheader("Summary Generated:")
        st.write(summary_text.text)
    
if __name__ == "__main__":
    main()
 
