import ai
import audio_maker
import pygame
import speech

num = 1

pygame.init()

n = True
while n:
    query = input("-> ")
    if query == "e":
        exit()
    if query =="":
        query = speech.listen_audio()
    response = ai.generate_response(query)
    audio_maker.generate_speech(response, "audio"+str(num)+".mp3")
    pygame.mixer.music.load("audio"+str(num)+".mp3")
    num += 1
    j = True
    while j:
        pygame.mixer.music.play()
        x = input("command: ")
        if x == "e":
            j = False
        if x == "p":
            pygame.mixer.music.play()