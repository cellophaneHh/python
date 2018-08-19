import tesserocr
from PIL import Image
import os


IMAGE_PATH = "./resources"

# 过滤获得所有问津
images = filter(lambda x: x.endswith('.jpeg'), os.listdir(IMAGE_PATH))

count = 0
count_correct = 0
for image in images:
    count += 1
    real_result = os.path.splitext(image)[0].strip()

    image_obj = Image.open(os.path.join(IMAGE_PATH, image))
    # 转换为灰度图像
    image_obj = image_obj.convert('L')
    # 对图像进行二值化
    threshold = 150  # 调节阈值使结果更加清晰
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image_obj = image_obj.point(table, '1')

    # image_obj.show()
    tesserocr_result = tesserocr.image_to_text(image_obj).strip()
    if real_result == tesserocr_result.lower():
        count_correct += 1

print()
print('样本数: {}'.format(str(count)))
print('识别正确数: {}'.format(str(count_correct)))
print('正确率: {:.2%}'.format((count_correct) / count))
