import pygame
import threading
import time

pygame.mixer.init()
is_ringing = False  # The flag that prevents overlapping

def _play_thread(sound_file):
    global is_ringing
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        # Wait until the sound is actually finished
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    finally:
        is_ringing = False # Reset the flag so it can ring again

def play_bell_non_blocking(sound_file):
    global is_ringing
    if not is_ringing:
        is_ringing = True
        # Create and start the thread
        t = threading.Thread(target=_play_thread, args=(sound_file,))
        t.daemon = True # Means the thread dies if the main script stops
        t.start()

def play_bell(sound_file):
    print("--- DING DONG! ---")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    
    # Optional: Wait for the sound to finish so it doesn't cut off
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)