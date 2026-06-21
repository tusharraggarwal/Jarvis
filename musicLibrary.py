
import webbrowser

def play(song):
    url=f"https://www.youtube.com/results?search_query={song}"
    webbrowser.open(url)