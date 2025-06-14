import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey sir, how can I help you")
        return "Hey sir, how can I help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir")
        return "Good morning sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = str(current_time.hour) + " Hour : " + str(current_time.minute) + " Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"

    elif "weather" in user_data:
        try:
            ans = weather.weather()
            text_to_speech.text_to_speech(ans)
            return ans
        except:
            text_to_speech.text_to_speech("Sorry, I couldn't fetch the weather")
            return "Sorry, I couldn't fetch the weather"

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"


