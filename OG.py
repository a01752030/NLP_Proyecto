import streamlit as st
import openai
import whisper
from dotenv import load_dotenv

load_dotenv()

openai.api_key = "GPT_KEY"

def transcribe_audio():
    try:
        model = whisper.load_model("base")
        file_path = 'MA1.m4a'
        transcript = model.transcribe(file_path)
        return transcript["text"]
    except Exception as e:
        st.error(f"Error durante la transcripción: {e}")
        return ""

def custom_chatgpt(user_input):
    messages = [
        {"role": "system", "content": "You are an office administrator, summarize the text in key points"},
        {"role": "user", "content": user_input},
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]
        return chatgpt_reply
    except Exception as e:
        st.error(f"Error in ChatGPT response: {e}")
        return ""

# Streamlit app
def main():
    st.title("Transcripcion de audio y resumen")

    st.text("Audio en cuestion:")
    st.audio('MA1.m4a', format='audio/m4a')

    if st.button("Transcribir y resumir"):
        st.text("Cargando...")

        transcription = transcribe_audio()

        summary = custom_chatgpt(transcription)

        st.text("Transcripción:")
        st.write(transcription)

        st.text("Resumen:")
        st.write(summary)

        st.text("Terminado!!")

if __name__ == "__main__":
    main()