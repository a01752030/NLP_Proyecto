import openai
import whisper
from dotenv import load_dotenv


openai.api_key = "GPT-KEY"

def load_whisper_model():
    try:
        model = whisper.load_model("base")
        return model
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        return None

def transcribe_audio(model, file_path):
    try:
        transcript = model.transcribe(file_path)
        return transcript['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""
def custom_chatgpt(user_input):
    messages = [{"role": "system", "content": "You are an office administrator, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]
        return chatgpt_reply
    except Exception as e:
        print(f"Error in ChatGPT response: {e}")
        return ""

# Main Execution
model = load_whisper_model()
if model:
    file_path = 'MA2.m4a'
    transcription = transcribe_audio(model, file_path)
    print(transcription)
    print('#######################################')
    summary = custom_chatgpt(transcription)
    print(summary)

