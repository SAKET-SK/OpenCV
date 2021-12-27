import cv2


def get_frames(video):
    def getFrame(x):
        video.set(cv2.CAP_PROP_POS_MSEC, x * 1000)
        hasFrames, image = video.read()
        if hasFrames:
            cv2.imwrite(str(count) + ".jpg", image)
        return hasFrames

    sec = 0
    frameRate = 1  
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)


