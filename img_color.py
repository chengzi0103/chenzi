import numpy as np
import cv2

img = cv2.imread(r'C:\Users\chenc\Desktop\py_file\data\example01754\groundtruth\output0.png', -1)
color_txt = r'C:\Users\chenc\Desktop\py_file\color6.txt'
with open(color_txt, 'r') as f:
    color_data = f.readlines()
    print(color_data)
img_zeros = np.ones((460, 460, 3))
# color_data.reverse()
# color_data = ['68,85,2,255,6','51,68,134,255,2','85,102,3,149,2','85,102,255,255,9']
# color_data = ['85,102,255,255,5']
# color_data = ['85,102,193,1,0']
for img_zeros_sheape in range(0, img_zeros.shape[-1]):
    for color_ in color_data:
        try:
            color_ = color_.split(',')
            color_ = [int(data.replace('\n', '')) for data in color_]
            img_index = np.where((img > color_[0]) & (img <= color_[1]))
            if len(img_index[0]) == 0 and len(img_index[1]) == 0:
                # img_zeros[:, :, img_zeros_sheape][img_index] = 0
                continue
            img_zeros[:,:,2-img_zeros_sheape][img_index] = color_[img_zeros_sheape+2]
        except:
            print(color_data.index(color_))
cv2.imwrite('zz.png',img_zeros)

        # cs_data = np.array([[1, 2, 3, 4], [6, 2, 3, 2]])
        # x = np.where((cs_data >= 2) & (cs_data <= 5))
        # cs_data[x] = 0
