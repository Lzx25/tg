import cv2
import numpy as np
def pic():
    img = cv2.imread('YellowStick.jpg')#读图片
    blurred = cv2.GaussianBlur(img, (3, 3), 1)#高斯模糊
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)#bgr转化为hsv

    lower_red = np.array([26, 43, 46])
    upper_red = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)#分割出黄色杠
    mask = cv2.inRange(hsv, lower_red, upper_red)#分割出黄色杠

    result = cv2.medianBlur(mask, 1)#中值滤波去噪
    kenerl = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 6))
    dst = cv2.erode(result, kenerl)#腐蚀
    dst1 = cv2.dilate(dst, kenerl)#膨胀
    cv2.imshow('dst1', dst1)
    cv2.imwrite('ezt.jpg', dst1)

    contours, hierarchy = cv2.findContours(dst1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#查找轮廓
    x, y, w, h = cv2.boundingRect(dst1)
    img1 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)#画出外接矩形
    cv2.imshow('img1', img1)
    cv2.imwrite('lk.jpg', img1)

    print('杠的中点为：', (x + w / 2, y + h/ 2))#打印杠的中心坐标
    cv2.waitKey(0)


if __name__ == '__main__':
    pic()
