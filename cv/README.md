# BZU Workshop - Spring 2023

<p align="center">
<picture>
  <img alt="Purpose Logo" src="../purpose_logo.png" width="20%" hight="20%" >
</picture>
</p>

## Computer Vision

Let's use <a href="https://github.com/MeqdadDev/detectors-world">Detectors World</a> package to build a computer vision application that uses hand detection to play <a href="https://chromedino.com/">T-Rex Dino Game</a>.

### Hand Detection Program

```python
from detectors_world import DetectorCreator
import cv2 as cv

cap = cv.VideoCapture(0)

creator = DetectorCreator()
hand = creator.getDetector("hand")

while True:
    status, img = cap.read()
    hand.detect(img, drawOnHand=True)
    landmarks = hand.locate(img, drawOnHand=True, handsNumber=1)
    cv.imshow("Hand Detection", img)
    cv.waitKey(1)
```

### Tracking Index Finger

</br>

<p align="center">
<picture>
  <img alt="Hand Landmarks" src="hand_landmarks.png" width="75%" hight="60%" >
</picture>
</p>

</br>

In our case, we want to track the 8th point (INDEX_FINGER_TIP).

`landmarks` list values represent: `[id, xVal, yVal]`.

### Hand Detection with T-Rex Dino Game

```python
import cv2 as cv
from pynput.keyboard import Key, Controller
from detectors_world import DetectorCreator

cap = cv.VideoCapture(0)

creator = DetectorCreator()

hand = creator.getDetector("hand")

keyboard = Controller()

def check_index_finger(landmarks):
    if len(landmarks) != 0:
        print(lms[4])
        if landmarks[8][2] < 150:
            keyboard.release(Key.down)
            print("UP")
            keyboard.press(Key.up)
        elif landmarks[8][2] > 350:
            keyboard.release(Key.up)
            print("DOWN")
            keyboard.press(Key.down)

while True:
    status, img = cap.read()
    hand.detect(img, drawOnHand=True)

    lms = hand.locate(img, drawOnHand=True, handsNumber=1)
    check_index_finger(lms)

    cv.line(img, (100, 150), (500, 150), (0, 255, 0), 1)
    cv.line(img, (100, 350), (500, 350), (0, 255, 0), 1)
    
    cv.imshow("T-Rex Dino Game", img)
    k = cv.waitKey(1)
    
    # if Esc is pressed -> Exit
    if k % 255 == 27:
        break
```

_Purpose Team_
