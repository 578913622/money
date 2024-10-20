#!/usr/bin/env python
# encoding=gbk

import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
equalizeHist��ֱ��ͼ���⻯
����ԭ�ͣ� equalizeHist(src, dst=None)
src��ͼ�����(��ͨ��ͼ��)
dst��Ĭ�ϼ���
'''

# ��ȡ�Ҷ�ͼ��
img = cv2.imread("lenna.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("image_gray", gray)

# �Ҷ�ͼ��ֱ��ͼ���⻯
dst = cv2.equalizeHist(gray)

# ֱ��ͼ
hist = cv2.calcHist([dst],[0],None,[256],[0,256])
# [dst]:
# ����һ������ͼ�����ݵ��б�������������У�dst ��һ��ͼ��ͨ���ǵ�ͨ�����ͨ��ͼ�񣩣�������Ҫ�������ͼ���ֱ��ͼ��
# [0]:
# �������ָ��Ҫ����ֱ��ͼ��ͨ�����������ڻҶ�ͼ��ͨ��ʹ�� 0 ����ʾ��һͨ����Ҳ��Ψһͨ����������ǲ�ɫͼ�񣬿���ʹ�� 0, 1, 2 ���ֱ��ʾ��ɫ����ɫ�ͺ�ɫͨ����
# None:
# ���������������ģ�ġ������None ��ʾ���ǲ�ʹ���κ���ģ��Ҳ����˵�����ǽ���������ͼ���ֱ��ͼ��
# [256]:
# �������ָ��ֱ��ͼ�Ĵ�С�������256 ��ʾ������Ҫ����һ������ 256 �� bin ��ֱ��ͼ��ͨ�����ڱ�ʾ����ֵ�� 0 �� 255 �ķֲ���
# [0, 256]:
# �������������ÿ�� bin �ķ�Χ���������Χ�Ǵ� 0 �� 256������ζ��ÿ�� bin ����Ӧ��һ������ֵ��0-255����

plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()

cv2.imshow("Histogram Equalization", np.hstack([gray, dst]))
cv2.waitKey(0)


'''
# ��ɫͼ��ֱ��ͼ���⻯
img = cv2.imread("lenna.png", 1)
cv2.imshow("src", img)

# ��ɫͼ����⻯,��Ҫ�ֽ�ͨ�� ��ÿһ��ͨ�����⻯
(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# �ϲ�ÿһ��ͨ��
result = cv2.merge((bH, gH, rH))
cv2.imshow("dst_rgb", result)

cv2.waitKey(0)
'''
