import cv2

videostream = cv2.VideoCapture(0)


def main():
    while True:
        check, frame = videostream.read()
        #color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #color = cv2.GaussianBlur(color,(21, 21),0)
        cv2.imshow('Live', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    videostream.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()

