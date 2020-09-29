import cv2

cap = cv2.VideoCapture(0)
# 0 is 1st devic like web camera, second device will be 1, third device will be 2
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# foourcc is video file format
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# 20 is frame per second, (640, 480) is frame size

# print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    # ret is frame capture success or not

    if ret == True:
        # frame capture success
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # convert frame to grayscale color
        cv2.imshow('frame', gray_frame)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            # q is q key
            break
    else:
        # frame capture not success
        break

cap.release()
out.release()
cv2.destroyAllWindows()