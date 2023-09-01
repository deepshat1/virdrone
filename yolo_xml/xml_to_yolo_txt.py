# -*- coding: utf8 -*-
import glob
import os
import xml.etree.ElementTree as ET

#  类名
class_names = ['Broken insulator', 'Flashover damage insulator', 'insulator-Pollute']


#  转换一个xml文件为txt
def single_xml_to_txt(xml_file,file):

    tree = ET.parse(xml_file)
    root = tree.getroot()   # 获取根节点
    #  保存的txt文件路径
    txt_file = r'D:\data\insulator\labels\train' + '\\' + file.split('.')[0] + '.txt'
    with open(txt_file, 'w') as txt_file:
        for member in root.findall('object'):
            # filename = root.find('filename').text
            picture_width = int(root.find('size')[0].text)
            picture_height = int(root.find('size')[1].text)
            class_name = member[0].text
            #  类名对应的index
            class_num = class_names.index(class_name)

            box_x_min = float(member[4][0].text)  # 左上角横坐标
            #print(box_x_min)
            box_y_min = float(member[4][1].text)  # 左上角纵坐标
            box_x_max = float(member[4][2].text)  # 右下角横坐标
            box_y_max = float(member[4][3].text)  # 右下角纵坐标
            # 转成相对位置和宽高
            x_center = str((box_x_min + box_x_max) / (2 * picture_width))[0:8]
            y_center = str((box_y_min + box_y_max) / (2 * picture_height))[0:8]
            width = str((box_x_max - box_x_min) / (picture_width))[0:8]
            height = str((box_y_max - box_y_min) / (picture_height))[0:8]
            print(class_num, x_center, y_center, width, height)
            txt_file.write(str(class_num) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(
                height) + '\n')


#  转换文件夹下的所有xml文件为txt
def dir_xml_to_txt(path):
    i = 1
    path += '\\'
    print(path)

    fileList = os.listdir(path)
    #print(fileList)
    for file in fileList:
        #print(file)
        xml_file = path + file
        single_xml_to_txt(xml_file,file)

    # for xml_file in glob.glob(path + '*.xml'):
    #     print("processing {}, {}".format(i, xml_file + '.xml'))
    #     single_xml_to_txt(xml_file)
    #     i += 1


def main(path):
    dir_xml_to_txt(path)


if __name__ == '__main__':
    #  xml文件路径
    path = r'D:\data\insulator\labels_xml\train' # xml文件存放地址
    # path = '/media/xavier/SSD256/global_datasets/BDD00K/bdd100k/Annotations/val/'
    main(path)
