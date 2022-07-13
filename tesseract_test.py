import cv2
import pytesseract

# call the tesseract_OCR path
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Color and thickness bounding box of image
BCOLOR = (255, 0, 255)
THICKNESS = 4
# Read image from path
img = cv2.imread("E:/Photo/31.jpg")
cap = cv2.VideoCapture('E:/Photo/card.mp4')
if (cap.isOpened() == False):
    print("Error opening video  file")
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            cap = cv2.cvtColor( cap, cv2.COLOR_BGR2GRAY)
            # Crop the object to detect, x, y are the coordinate, w, h are the width and height
            x,y,w,h = cv2.selectROI("Region of interest", cap)
            print(x,y,w,h)

            cropped = img[y:y+h, x:x+w]
            cv2.imshow("Cropped", cropped)
            cv2.waitKey(0)
# Convert image to Binary
ret, thresh2 = cv2.threshold(cropped,30, 255, cv2.THRESH_BINARY_INV)
# Read text inside the box cropped
text = pytesseract.image_to_string(cropped)
# Print text
print("Value of scratch card is:",text)

# Drawing box around object and put text
cv2.rectangle(img_color, (x,y), (x+w,y+h),(255,255,0), 2)
cv2.putText(img_color,"Here is the value of scratch card", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0,255), 2)

# Show result on screen
cv2.imshow("Original Image", img_color)
cv2.waitKey(0)