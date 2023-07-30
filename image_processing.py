import cv2
import numpy as np
import os
import utils
import win32gui, win32ui, win32con

# This function loads the images of the figures to be detected
# Returns:
# - a dictionary containing the images of the figures
def load_images():
    images = {}
    images['master'] = {}
    images['monster'] = {}
    images['suit'] = {}
    for file in os.listdir('./images'):
        if file.endswith('.PNG'):
            key, rarity = file.split('_')
            rarity = rarity.split('.')[0]
            images[key][rarity] = cv2.imread(f'images/{file}')
    return images

# This function compares an image with the loaded images of the figures
# Parameters:
# - img: a screenshot of the game screen
# Returns:
# - a dictionary containing the similarities between the image and the loaded images of the figures
def compare_images(img):
    similarities = {}
    for key, rarities in utils.images.items():
        for rarity, image in rarities.items():
            img_resized = cv2.resize(img, (image.shape[1], image.shape[0]))
            ssim = cv2.matchTemplate(img_resized, image, cv2.TM_CCOEFF_NORMED)
            similarities[f"{key}_{rarity}"] = ssim[0][0]
    return similarities

# This function checks if an image matches a certain figure
# Parameters:
# - img: a screenshot of the game screen
# - key: a string representing the type of figure to be matched
# - rarity: a string representing the rarity of the figure to be matched
# Returns:
# - True if the image matches the figure, False otherwise
def is_match(img, key, rarity):
    image = utils.images[key][rarity]
    img_resized = cv2.resize(img, (image.shape[1], image.shape[0]))
    ssim = cv2.matchTemplate(img_resized, image, cv2.TM_CCOEFF_NORMED)
    if ssim[0][0] > 0.60:
        return True
    else:
        return False

# This function stores the icons of the figures in a directory
# Parameters:
# - img: a screenshot of the game screen
# - areas: a dictionary containing the areas of the game screen where the icons are located
def store_icons(img, areas):
    for group, items in areas.items():
        x1, y1, x2, y2 = items['icono']
        cropped = img[y1:y2, x1:x2]
        cv2.imwrite(f'icons/{group}.PNG', cropped)

# This function gets the type of a figure from its icon
# Parameters:
# - img: a screenshot of the game screen
# - icono: a tuple representing the area of the game screen where the icon is located
# Returns:
# - a list containing the type and rarity of the figure
def get_type(img, icono):
    x1, y1, x2, y2 = icono
    similarity = compare_images(img[y1:y2, x1:x2])
    return max(similarity, key=similarity.get).split('_')

def get_slots(img, icono):
    x1, y1, x2, y2 = icono
    cropped = img[y1:y2, x1:x2]
    slots = 4 - len([x for x in [83, 63, 40, 17] if img[90, x, 2] < 150])
    return slots
            

# This function checks if an image matches a certain figure type and rarity
# Parameters:
# - img: a screenshot of the game screen
# - icono: a tuple representing the area of the game screen where the icon is located
# - typen: a string representing the type of figure to be matched
# - rarity: a string representing the rarity of the figure to be matched
# Returns:
# - True if the image matches the figure type and rarity, False otherwise  
def check_type(img, icono, typen, rarity):
    x1, y1, x2, y2 = icono
    return is_match(img[y1:y2, x1:x2], typen, rarity)

# This function checks if the game is stuck by checking the color of a pixel
# Parameters:
# - img: a screenshot of the game screen
# Returns:
# - True if the game is stuck, False otherwise
def detect_stuck(img):
    #check the pixel 436,218 it must be of color F0F0F0, if it is not, then the game is stuck
    #print(img[218,436])
    if img[218,436,0] != 215 or img[218,436,1] != 141 or img[218,436,2] != 251:
        return True
    return False

# This function captures a screenshot of the game window, you're not suposed to understand this.
# Returns:
# - a screenshot of the game window as a numpy array
def capture_window():
    hwnd = win32gui.FindWindow(None, utils.window_name)
    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    width, height = right - left, bottom - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)
    win32gui.BitBlt(saveDC.GetSafeHdc(), 0, 0, width, height, hwndDC, 0, 0, win32con.SRCCOPY | 0x40000000)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    img = np.fromstring(bmpstr, dtype='uint8')
    img.shape = (bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4)
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img