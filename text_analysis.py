import cv2
import pytesseract
from difflib import SequenceMatcher
from utils import stats, translations, language

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# This function extracts the price of an item from a screenshot of the game screen
# Parameters:
# - img: a screenshot of the game screen
# - area: a tuple representing the area of the game screen where the price is located
# Returns:
# - a float representing the price of the item
def extract_price(img, area):
    x1, y1, x2, y2 = area
    cropped = img[y1:y2, x1:x2]

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(thresh, lang=language, config='--psm 6 -c tessedit_char_whitelist=0123456789,')
    text = float(text.replace(',', '').replace('\n', '').strip())

    return text

# This function analyzes a text from a screenshot of the game screen
# Parameters:
# - img: a screenshot of the game screen
# - area: a tuple representing the area of the game screen where the text is located
# Returns:
# - a string representing the analyzed text
def analyze_text(img, area):
    x1, y1, x2, y2 = area
    cropped = img[y1:y2, x1:x2]

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(thresh, lang=language, config='--psm 11 -c preserve_interword_spaces=1 -c tessedit_char_whitelist= ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%')
    return text.replace('\n', ' ').replace("'", '').replace('|', ' ').strip()

# This function recognizes the type of stat from a string
# Parameters:
# - text: a string representing the stat to be recognized
# Returns:
# - a string representing the recognized stat
def recognize_stat(text):
    text = ''.join([i for i in text if not i.isdigit()]).replace('\n', '')

    similarities = {}
    for key, value in stats.items():
        ratio = SequenceMatcher(None, text.lower(), value[language].lower()).ratio()
        similarities[key] = ratio
    return max(similarities, key=similarities.get)

# This function translates a string from Spanish to English
# Parameters:
# - text: a string representing the text to be translated
# Returns:
# - a string representing the translated text
def translate_eng(text):
    return translations[max(translations, key=lambda x: SequenceMatcher(None, text.lower(), x.lower()).ratio())]