import webbrowser
import pywhatkit

while True:
    query = input("Me:")
    if "hello" in query:
        print("hello dear")

    elif "name" in query:
        print("i am bot")

    elif "exit" in query:
        print("ok i am going offline")
        exit()

    elif'open google' in query:
        print("ok opening google")
        print("what should i search on google")
        search = input("Me:")
        pywhatkit.search(search)

    elif'open instagram' in query:
        print("ok opening instagram")
        webbrowser.open("http://www.instagram.com")

    elif'open youtube' in query:
        print("ok opening youtube")
        print("ok opening yutube")
        print("what i should i search on youtube")

        search = input("Me:")
        pywhatkit.playonyt(search)