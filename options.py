# Author: Tiana Madison
# Date: 25 April 2022
# Class: CS 4500
# ========================================================================================================
# Description: This program handles the options menu.
# =========================================================================================================
# Central Data Structures used: Dictionaries
# =========================================================================================================
# External Files: json (There is no need to add anything, the program will create the necessary files)
# =========================================================================================================
# External Sources used: Python 3.10.4 Documentation: https://docs.python.org/3/library/json.html
# Pygame Documenation: https://www.pygame.org/docs/ref/mixer.html 
# =========================================================================================================
import re
import pygame
import json
import sys
import menu_button
from pygame.locals import *

# Setting up window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

def checkSounds():
    try:
        with open("./options.json", "r+", encoding="utf-8") as f:
            sound_options = json.load(f)

    except FileNotFoundError:
        sound_options = {
                            "music": True,
                            "sounds": True       
                        }

        f = open("./options.json", "w") # Create the new local storage file
        json.dump(sound_options, f, indent=4) # Save the data to the new json file
    
    return sound_options

def control_sound_volume(default):
    sound_options = checkSounds()
    if sound_options["sounds"] == False:
        volume = 0
    else:
        volume = default
    return volume

def toggle_volume_music():
    options = checkSounds()
    if options["music"] == False:
        options["music"] = True
        pygame.mixer.music.set_volume(0.7)
    else:
        options["music"] = False
        pygame.mixer.music.set_volume(0)
    
    f = open("./options.json", "w")
    json.dump(options, f, indent=4)

def toggle_volume_sound():
    options = checkSounds()
    if options["sounds"] == False:
        options["sounds"] = True
    else:
        options["sounds"] = False
    
    f = open("./options.json", "w")
    json.dump(options, f, indent=4)

def get_music_status(background_color):
    # Change the sound status text based on whether sound is muted or not
    options = checkSounds()
    font = pygame.font.SysFont(None, 50)
    
    if options["music"] == False:
        status = "OFF"
        text_color = Color(185, 0, 0)
    else:
        status = "ON"
        text_color = Color(0, 209, 0)
    
    music_status_object = font.render(status, True, text_color, background_color)
    return music_status_object

def get_sound_status(background_color):
    # Change the sound status text based on whether sound is muted or not
    options = checkSounds()
    font = pygame.font.SysFont(None, 50)
    
    if options["sounds"] == False:
        status = "OFF"
        text_color = Color(185, 0, 0)
    else:
        status = "ON"
        text_color = Color(0, 209, 0)
    
    sounds_status_object = font.render(status, True, text_color, background_color)
    return sounds_status_object


def format_options(root, screen, options):
    # Setting up options menu appearance

    # Color List
    black = Color(0, 0, 0)
    blue = Color(58, 121, 227)
    light_blue = Color(30, 30, 230)
    lighter_blue = Color(80, 80, 245)
    brown = Color(100, 70, 50)
    green = Color(82, 216, 50)
    purple = Color(112, 65, 192)
    light_purple = Color(186, 156, 199)
    pink = Color(203, 165, 188)
    magenta = Color(172, 89, 188)
    teal = Color(41, 106, 131)
    light_teal = Color(98, 184, 208)

    BACKGROUND_COLOR = Color(34, 26, 92)
    SUB_BACKGROUND_COLOR = black
    TEXT_COLOR = Color(255, 255, 255)
    HEADER_COLOR = teal
    HEADER_COLOR_HARD = teal
    SUBHEADER_COLOR_EASY = teal
    SUBHEADER_COLOR_HARD = teal
    MESSAGE_BACKGROUND_COLOR = teal
    ENTRY_BACKGROUND_1 = Color(54, 154, 181)
    ENTRY_BACKGROUND_2 = light_teal

    # Font
    header_font = pygame.font.SysFont(None, 120)
    subheader_font = pygame.font.SysFont(None, 50)
    entry_font = pygame.font.SysFont(None, 40)

    # Surface building and positioning
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    background_sub_rect = Rect(screen_width/15, screen_height/15, screen_width - (screen_width/7.5), screen_height - (screen_height/5))
    header_zone = Rect(screen_width/11, screen_height/11, screen_width - (screen_width/5.5), screen_height - (screen_height/1.15))
    content_zone = Rect(screen_width/11, screen_height/4, screen_width - (screen_width/5.5), screen_height/1.8)

    # Header text
    header_text = "Options"
    music_text = "Music:"
    sounds_text = "Sounds:"

    # Setting up the main surfaces
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, SUB_BACKGROUND_COLOR, background_sub_rect)
    pygame.draw.rect(screen, HEADER_COLOR, header_zone)
    pygame.draw.rect(screen, HEADER_COLOR, content_zone)


    # Fill in the header information
    header_object = header_font.render(header_text, True, TEXT_COLOR, HEADER_COLOR)
    header_rect = header_object.get_rect()
    header_rect.center = ((screen_width/2), screen_height/6.5)
    screen.blit(header_object, header_rect)

    # Fill in the options menu contents
    music_object = subheader_font.render(music_text, True, TEXT_COLOR, black)
    music_rect = music_object.get_rect()
    music_rect.center = ((screen_width/2.3), screen_height/2.55)
    screen.blit(music_object, music_rect)

    sounds_object = subheader_font.render(sounds_text, True, TEXT_COLOR, black)
    sounds_rect = sounds_object.get_rect()
    sounds_rect.center = ((screen_width/2.3), screen_height/2.1)
    screen.blit(sounds_object, sounds_rect)

    box_unticked = pygame.image.load(r'Images/Box_unticked.png')
    box_ticked = pygame.image.load(r'Images/Box_ticked.png')
    box_unticked_hovered = pygame.image.load(r'Images/Box_unticked_hovered.png')
    box_ticked_hovered = pygame.image.load(r'Images/Box_ticked_hovered.png')
    
    # Music status plates
    music_status_object = get_music_status(black)
    music_status_rect = music_status_object.get_rect()
    music_status_rect.center = (screen_width/2, screen_height/2.55)
    screen.blit(music_status_object, music_status_rect)

    # Sound status plates
    sounds_status_object = get_sound_status(black)
    sounds_status_rect = sounds_status_object.get_rect()
    sounds_status_rect.center = (screen_width/2, screen_height/2.1)
    screen.blit(sounds_status_object, sounds_status_rect)

    right_sound_button_unticked = menu_button.Custom_Button(screen_width/1.9, screen_height/2.2, box_unticked, box_unticked_hovered, 0.03, 0.048)
    right_sound_button_ticked = menu_button.Custom_Button(screen_width/1.9, screen_height/2.2, box_ticked, box_ticked_hovered, 0.03, 0.048)
    right_music_button_unticked = menu_button.Custom_Button(screen_width/1.9, screen_height/2.75, box_unticked, box_unticked_hovered, 0.03, 0.048)
    right_music_button_ticked = menu_button.Custom_Button(screen_width/1.9, screen_height/2.75, box_ticked, box_ticked_hovered, 0.03, 0.048)

    # Menu Noises
    click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')
    volume = control_sound_volume(0.5)
    pygame.mixer.Sound.set_volume(click_sound, volume)
    
    options = checkSounds()
    if options["sounds"] == False:
        if right_sound_button_unticked.draw_custom_button(screen):
            toggle_volume_sound()
            volume = control_sound_volume(0.5)
            pygame.mixer.Sound.set_volume(click_sound, volume)
            pygame.mixer.Sound.play(click_sound)
            pygame.time.wait(200)
    else:
        if right_sound_button_ticked.draw_custom_button(screen):
            toggle_volume_sound()
            volume = control_sound_volume(0.5)
            pygame.mixer.Sound.set_volume(click_sound, volume)
            pygame.mixer.Sound.play(click_sound)
            pygame.time.wait(200)
        
    if options["music"] == False:
        if right_music_button_unticked.draw_custom_button(screen):
            toggle_volume_music()
            pygame.mixer.Sound.play(click_sound)
            pygame.time.wait(200)
    else:
        if right_music_button_ticked.draw_custom_button(screen):
            toggle_volume_music()
            pygame.mixer.Sound.play(click_sound)
            pygame.time.wait(200)
    


def display_options_menu(root, screen, options):
    # Main loop that controls the options page
    # Takes the root and screen from the main file as parameters
    running = True
    FPS = 60 # Locks the FPS on the screen to this value
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        format_options(root, screen, options)

        # Menu Noises
        click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')
        volume = control_sound_volume(0.5)
        pygame.mixer.Sound.set_volume(click_sound, volume)
        
        # Back to main menu button
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        main_menu_button = menu_button.Back_Button(x=width * 0.07, y=height * 0.9)
        
        if main_menu_button.draw_back_button(screen):
            pygame.mixer.Sound.play(click_sound)
            running = False

        pygame.display.update()
    
    return

pygame.quit()