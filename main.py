try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import numpy as np
import cv2

img = Image.open('test.png')
processed_image = np.asarray(img)
processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
processed_image = cv2.threshold(processed_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
text = pytesseract.image_to_string(processed_image, config='--psm 7').strip()
print(text)