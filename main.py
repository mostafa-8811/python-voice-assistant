import sys
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty("rate", 175)  # Set speaking speed


def speak(text: str) -> None:
    """Converts text to speech and prints output to console."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def get_time() -> None:
    """Announces the current time."""
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def search_wikipedia(query: str) -> None:
    """Searches Wikipedia and reads a two-sentence summary."""
    try:
        speak(f"Searching Wikipedia for {query}...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results for that topic. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find any Wikipedia page matching that query.")
    except Exception:
        speak("I encountered an error while accessing Wikipedia.")


def recognize_speech(recognizer: sr.Recognizer, mic: sr.Microphone) -> str | None:
    """Captures audio input from the microphone and converts it to text."""
    with mic as source:
        print("\nListening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return None


def process_command(command: str, recognizer: sr.Recognizer, mic: sr.Microphone) -> bool:
    """Processes incoming text commands. Returns False to exit the application loop."""
    if "time" in command:
        get_time()
    elif "wikipedia" in command:
        # Extract query if included in command, otherwise prompt user
        query = command.replace("wikipedia", "").replace("search", "").strip()
        if not query:
            speak("What would you like to search on Wikipedia?")
            query = recognize_speech(recognizer, mic)

        if query:
            search_wikipedia(query)
    elif any(word in command for word in ["exit", "stop", "bye", "quit"]):
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I don't recognize that command.")

    return True


def start_voice_assistant():
    """Main execution entry point."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Calibrating background noise... Please wait.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    speak("Hello! I am your voice assistant. How can I help you?")

    running = True
    while running:
        command = recognize_speech(recognizer, mic)
        if command:
            running = process_command(command, recognizer, mic)


if __name__ == "__main__":
    start_voice_assistant()
