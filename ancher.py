import utils.autoanchor as autoAC

# 对数据集重新计算 anchors
new_anchors = autoAC.kmean_anchors('/home/yolov7-yiwu/data/yiwu.yaml', 9, 640, 5.0, 1000, True)
print(new_anchors)
