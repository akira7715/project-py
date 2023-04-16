import cv2
from cvzone.HandTrackingModule import HandDetector
import webbrowser
import time

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

ur1 = "https://www.kochi-tech.ac.jp/"
ur2 = "https://www.kochi-tech.ac.jp/student/"
ur3 = "https://www.youtube.com/"
ur4 = "https://www.amazon.co.jp/?&tag=hydraamazonav-22&ref=pd_sl_7ibq2d37on_e&adgrpid=56100363354&hvpone=&hvptwo=&hvadid=618607352532&hvpos=&hvnetw=g&hvrand=6437673625145908627&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1009694&hvtargid=kwd-10573980&hydadcr=27922_14600116&gclid=EAIaIQobChMI5KO58MPg_QIVX9xMAh3xvAHFEAAYASAAEgIbhvD_BwE"
ur5 = "https://www.python.jp/"

page = 0

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                webbrowser.open(ur1, 1)
                time.sleep(3)
                page += 1
                if page == 3:
                    break
            if fingerup == [0, 1, 1, 0, 0]:
                webbrowser.open(ur2, 1)
                time.sleep(3)
                page += 1
                if page == 3:
                    break
            if fingerup == [0, 1, 1, 1, 0]:
                webbrowser.open(ur3, 1)
                time.sleep(3)
                page += 1
                if page == 3:
                    break
            if fingerup == [0, 1, 1, 1, 1]:
                webbrowser.open(ur4, 1)
                time.sleep(3)
                page += 1
                if page == 3:
                    break
            if fingerup == [1, 1, 1, 1, 1]:
                webbrowser.open(ur5, 1)
                time.sleep(3)
                page += 1
                if page == 3:
                    break
             
    cv2.imshow("Video",img)
    key = cv2.waitKey(1)
    if key == ord("q") or key == ord("Q"):
        break

#https://github.com/vamshi6763/fingers_count_using_openCV/blob/fd9b57355a3a8463a445e81663fd2e46a2741838/main.py