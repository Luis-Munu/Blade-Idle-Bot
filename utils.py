import json
import random
from time import sleep

import cv2
import win32api
import win32con
import win32gui

from image_processing import load_images

type_safety = True
language = 'eng'

# Function used to show the areas of the game screen that are being captured
# Parameters:
# - img: a screenshot of the game screen
# - areas: a dictionary containing the areas of the game screen to be shown
def show_areas(img, areas):
    for group, items in areas.items():
        for name, coords in items.items():
            x1, y1, x2, y2 = coords
            cropped = img[y1:y2, x1:x2]
            cv2.imshow(f"{group}_{name}", cropped)
            cv2.waitKey(0)

    cv2.destroyAllWindows()
    
# Function used to load the filters specified by the user
def load_filters():
    return json.load(open('figures.json', 'r'))

# Function used to click on the coordinates specified by the user, uses relative coordinates to HD-Player.
# To calculate the relative coordinates to HD-Player, substract 60 to the y axis of the relative coordinates of BlueStacks.
# Parameters:
# - coords: a list of tuples representing the coordinates to be clicked
def click_coords(coords):
    window = win32gui.FindWindow(None, window_name)
    child_window = win32gui.FindWindowEx(window, None, None, "HD-Player")
    win32gui.SendMessage(window, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
    coords = [(coord[0] + random.randint(-3, 3), coord[1] + random.randint(-3, 3)) for coord in coords]
    
    for coord in coords:
        click = win32api.MAKELONG(coord[0], coord[1])
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
        sleep(0.1)
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONUP, None, click)
        sleep(random.randint(2, 3))
        
def send_keystroke(key):
    window = win32gui.FindWindow(None, window_name)
    child_window = win32gui.FindWindowEx(window, None, None, "HD-Player")
    win32gui.SendMessage(window, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
    win32gui.PostMessage(child_window, win32con.WM_KEYDOWN, key, 0)
    sleep(0.3)
    win32gui.PostMessage(child_window, win32con.WM_KEYUP, key, 0)
    sleep(random.randint(1, 2))

def come_back_soft():
    window = win32gui.FindWindow(None, window_name)
    child_window = win32gui.FindWindowEx(window, None, None, "HD-Player")
    win32gui.SendMessage(window, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
    print("Soft Resetting")
    # send ESCAPE KM key 3 times 
    for i in range(3):
        win32gui.PostMessage(window, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
        sleep(0.3)
        win32gui.PostMessage(window, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)
        sleep(0.1)
    # define list of coordinates and sleep times
    coords = [(215, 673, 0.6), (330, 660, 4), (560, 580, 1), (250, 1030, 3)]
    # iterate over coordinates and perform clicks with sleep times
    for coord in coords:
        click = win32api.MAKELONG(coord[0], coord[1])
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
        sleep(0.1)
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONUP, None, click)
        sleep(coord[2])
    sleep(1)
    
def come_back_hard():
    window = win32gui.FindWindow(None, window_name)
    child_window = win32gui.FindWindowEx(window, None, None, "HD-Player")
    win32gui.SendMessage(window, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
    print("Hard resetting")
    click = win32api.MAKELONG(640, 1115)
    win32gui.PostMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
    sleep(0.1)
    win32gui.PostMessage(window, win32con.WM_LBUTTONUP, None, click)
    sleep(0.7)
    # define list of coordinates and sleep times
    coords = [(530, 190, 3), (810, 350, 30), (310, 600, 10), (306, 567, 15)]
    # iterate over coordinates and perform clicks with sleep times
    for coord in coords:
        click = win32api.MAKELONG(coord[0], coord[1])
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
        sleep(0.1)
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONUP, None, click)
        sleep(coord[2])
    come_back_soft()
    # define list of coordinates and sleep times
    coords = [(389, 325, 0.4), (400, 410, 1)]
    # iterate over coordinates and perform clicks with sleep times
    for coord in coords:
        click = win32api.MAKELONG(coord[0], coord[1])
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
        sleep(0.1)
        win32gui.PostMessage(child_window, win32con.WM_LBUTTONUP, None, click)
        sleep(coord[2])    
    
    
            

################################# CONSTANTS #################################

images = load_images()
bought_figures = []
filters = load_filters()

window_name = "BlueStacks App Player"

areas = {
    '1': {
        'precio': (285, 460, 405, 490),
        'rareza': (130, 500, 220, 530),
        'stat': (220, 500, 600, 530),
        'rareza2': (130, 540, 220, 570),
        'stat2': (220, 540, 600, 570),
        'icono': (12, 428, 112, 528)
    },
    '2': {
        'precio': (285, 625, 405, 655),
        'rareza': (130, 665, 220, 695),
        'stat': (220, 665, 600, 695),
        'rareza2': (130, 705, 220, 735),
        'stat2': (220, 705, 600, 735),
        'icono': (12, 593, 112, 693)
    },
    '3': {
        'precio': (285, 795, 405, 825),
        'rareza': (130, 830, 220, 860),
        'stat': (220, 830, 600, 865),
        'rareza2': (130, 870, 220, 900),
        'stat2': (220, 870, 600, 905),
        'icono': (12, 758, 112, 858)
    },
    '4': {
        'precio': (285, 960, 405, 990),
        'rareza': (130, 990, 220, 1030),
        'stat': (220, 990, 600, 1035),
        'rareza2': (130, 1030, 220, 1070),
        'stat2': (220, 1030, 600, 1075),
        'icono': (12, 923, 112, 1023)
    }
}

market_options = {
    'Figure_rarity_base': (100, 320),
    'Figure_rarities': {
        'All': (100, 360),
        'Sky': (100,415),
        'God': (100, 465),
        'Mythic': (100, 510),
        'Legendary': (100, 560)
    },
    'Stat_rarities': {
        'God': (410, 260),
        'Mythic': (245, 260),
        'Legendary': (70, 260),
    },
    'Stat_button': (555, 300),
    'Stat_base': (70, 530),
    'Stat_single': (75, 390),
    'Stat_double': (330, 390),
    'Search_button': (300, 935),
    'Type_base': (100, 285),
    'Figure_types': {
        'All': (100, 320),
        'Monster': (100, 370),
        'Master': (100, 410),
        'Suit': (100, 460),
    },
    'Slots_base': (380, 280),
    'Slots': {
        'All': (380, 330),
        '1': (380, 380),
        '2': (380, 410),
        '3': (380, 460),
        '4': (380, 500)
    },
    'Price_base': (390, 330),
    'Price_low': (390, 410),
    'Accept_buy': (370, 938),
    'Reaccept_buy': (430, 667),
    'Remove_error_buy': (295,610),
}

stats = {
    'ATK': {
        'spa': 'Aumentar el Ataque %',
        'eng': 'Increase ATK %',
        'pos': (2,4)
    },
    'Figure ATK': {
        'spa': 'Mejorar el Ataque de la Figura %',
        'eng': 'Upgrade Figure ATK %',
        'pos': (2,7)
    },
    'Final ATK': {
        'spa': 'Mejorar el Ataque Final %',
        'eng': 'Upgrade Final ATK %',
        'pos': (1,1)
    },
    'HP': {
        'spa': 'Aumentar la Puntos de Vida %',
        'eng': 'Increase HP %',
        'pos': (1,5)
    },
    'Figure HP': {
        'spa': 'Mejorar los Puntos de Vida de la Figura %',
        'eng': 'Upgrade Figure HP %',
        'pos': (2,1)
    },
    'DEF': {
        'spa': 'DEF %',
        'eng': 'DEF %',
        'pos': (2,5)
    },
    'Figure DEF': {
        'spa': 'Mejorar la Defensa de la Figura %',
        'eng': 'Upgrade Figure DEF %',
        'pos': (1,2)
    },
    'Crit': {
        'spa': 'DAÑO CRÍTICO %',
        'eng': 'CRIT DMG %',
        'pos': (1,6)
    },
    'Super crit': {
        'spa': 'SUPER DAÑO CRÍTICO %',
        'eng': 'Super CRIT DMG %',
        'pos': (2,6)
    },
    'Hyper crit': {
        'spa': 'DAÑO HIPER CRÍTICO %',
        'eng': 'Hyper CRIT DMG %',
        'pos': (1,7)
    },
    'PEN': {
        'spa': 'PEN %',
        'eng': 'PEN %',
        'pos': (2,2)
    },
    'ACU': {
        'spa': 'PRECISIÓN %',
        'eng': 'ACU %',
        'pos': (1,3)
    },
    'Gold': {
        'spa': 'Aumentar el Oro %',
        'eng': 'Increase Gold %',
        'pos': (2,3)
    },
    'EXP': {
        'spa': 'Aumentar la EXP %',
        'eng': 'Increase EXP %',
        'pos': (1,4)
    }
}
translations = {
    'maestro': 'Master',
    'monstruo': 'Monster',
    'traje': 'Suit',
    'Magia': 'Magic',
    'Raro': 'Rare',
    'Épico': 'Epic',
    'Legendario': 'Legendary',
    'Mítico': 'Mythic',
    'Dios': 'God',
    'Cielo': 'Sky',
}

rarities = {
    'Sky': (100,415),
    'God': (100, 465),
    'Mythic': (100, 510),
    'Legendary': (100, 560),
}

stored_coords = {
    'Market': [(300, 230), (333,615), (283, 473), (315,407), (120, 230)],
    'Rarity': (100,320),
    'Buy': [(370,938), (430,667), (295,610)]
}