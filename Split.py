import os
import random
import shutil

# 定义源文件夹路径
src_dir = './number'

# 定义目标文件夹路径
dst_dir = './number2'

# 定义划分比例
ratio = 0.8

# 创建文件夹
if not os.path.exists(os.path.join(dst_dir)):
    os.makedirs(os.path.join(dst_dir))

# 将classes.txt文件挪到最外层文件夹中
classes_src_path = os.path.join(src_dir, 'labels', 'classes.txt')
classes_dst_path = os.path.join(dst_dir, 'classes.txt')
shutil.copy(classes_src_path, classes_dst_path)

# 创建images和labels文件夹
if not os.path.exists(os.path.join(dst_dir, 'images', 'train')):
    os.makedirs(os.path.join(dst_dir, 'images', 'train'))
if not os.path.exists(os.path.join(dst_dir, 'images', 'val')):
    os.makedirs(os.path.join(dst_dir, 'images', 'val'))
if not os.path.exists(os.path.join(dst_dir, 'labels', 'train')):
    os.makedirs(os.path.join(dst_dir, 'labels', 'train'))
if not os.path.exists(os.path.join(dst_dir, 'labels', 'val')):
    os.makedirs(os.path.join(dst_dir, 'labels', 'val'))

# 获取images文件夹中的所有文件名
image_files = os.listdir(os.path.join(src_dir, 'images'))

# 随机打乱文件名
random.shuffle(image_files)

# 计算分割点
split_point = int(ratio * len(image_files))

# 将文件分配到train和val文件夹中
for i, image_file in enumerate(image_files):
    # 源文件路径
    src_image_path = os.path.join(src_dir, 'images', image_file)
    src_label_path = os.path.join(src_dir, 'labels', image_file[:-4] + '.txt')
    # 目标文件路径
    if i < split_point:
        dst_image_path = os.path.join(dst_dir, 'images', 'train', image_file)
        dst_label_path = os.path.join(dst_dir, 'labels', 'train', image_file[:-4] + '.txt')
    else:
        dst_image_path = os.path.join(dst_dir, 'images', 'val', image_file)
        dst_label_path = os.path.join(dst_dir, 'labels', 'val', image_file[:-4] + '.txt')
    # 复制文件
    try:
        shutil.copy(src_image_path, dst_image_path)
    except Exception as e:
        print(f"Failed to copy image file {src_image_path} to {dst_image_path}: {e}")
    try:
        shutil.copy(src_label_path, dst_label_path)
    except Exception as e:
        print(f"Failed to copy label file {src_label_path} to {dst_label_path}: {e}")