import json
import xml.etree.ElementTree as ET
import os
import glob
import random
import shutil
class ConvertCoCo(object):

    START_BOUNDING_BOX_ID = 1

    def __init__(self, imgdir,savedir):
        self.imgdir = imgdir
        self.savedir = savedir


    def get(self,root, name):
        vars = root.findall(name)
        return vars

    def get_and_check(self,root, name, length):
        vars = root.findall(name)
        if len(vars) == 0:
            raise NotImplementedError('Can not find %s in %s.'%(name, root.tag))
        if length > 0 and len(vars) != length:
            raise NotImplementedError('The size of %s is supposed to be %d, but is %d.'%(name, length, len(vars)))
        if length == 1:
            vars = vars[0]
        return vars


    def get_filename_as_int(self,filename):
        try:
            filename = os.path.splitext(filename)[0]
            return int(filename)
        except:
            raise NotImplementedError('Filename %s is supposed to be an integer.'%(filename))

    def split_data(self,data,ratio):
        random.seed(20230312)
        random.shuffle(data)
        nrow = len(data)
        offset  = int(nrow * ratio)
        if offset != nrow:
            train_data = data[:offset]
            val_data = data[offset:]
            return {'train':train_data,'valid':val_data}
        else:
            return {'train':data,'valid':[]}
        

    def create_dir(self,path):
        if not os.path.exists(path):
            os.mkdir(path)

    def convert(self,ratio):
        """

        :param xml_list: 由xml文件名组成的列表['1.xml','2.xml']
        :param xml_dir:  原始存放xml文件夹路径
        :param json_file: 生成json文件的存放路径
        :return:
        """

        xml_f_list = list(glob.glob(self.savedir+"/*.xml"))

        xml_f_dict = self.split_data(xml_f_list,ratio)
        ID_dict = {'train':list(range(0,len(xml_f_dict['train']))),'valid':list(range(len(xml_f_dict['train']),len(xml_f_dict['train'])+len(xml_f_dict['valid'])))}

        for key,data in xml_f_dict.items():
            if data:
                json_dict = {"images":[], "type": "instances", "annotations": [],
                            "categories": []}
                categories = {}
                bnd_id = self.START_BOUNDING_BOX_ID

                annotations_dir = os.path.join(self.savedir,"annotations")#创建保存json文件的文件夹
                images_dir = os.path.join(self.savedir,"images")#创建保存图像文件的文件夹
                self.create_dir(annotations_dir)
                self.create_dir(images_dir)
                save_json_path = os.path.join(annotations_dir,key+'.json')#创建保存json文件

                for index, xml_f in enumerate(data) :
                    base_name = os.path.basename(xml_f).split('.')[0]
                    scr_img_path = glob.glob(os.path.join(self.imgdir,base_name)+'.*')
                    scr_img_path  = scr_img_path[0]
                    dist_img_path = os.path.join(images_dir,os.path.basename(scr_img_path))
                    shutil.copy(scr_img_path,dist_img_path)#复制图片到images文件夹中

                    tree = ET.parse(xml_f)
                    root = tree.getroot()
                    img_path = self.get(root, 'path')
                    if len(img_path) == 1:
                        filename = os.path.basename(img_path[0].text)
                    elif len(img_path) == 0:
                        filename = self.get_and_check(root, 'filename', 1).text
                    else:
                        raise NotImplementedError('%d paths found in %s'%(len(img_path), img_path))
                    ## The filename must be a number
                    # image_id = self.get_filename_as_int(filename)
                    image_id = int(ID_dict[key][index])
                    size = self.get_and_check(root, 'size', 1)
                    width = int(self.get_and_check(size, 'width', 1).text)
                    height = int(self.get_and_check(size, 'height', 1).text)
                    image = {'file_name': filename, 'height': height, 'width': width,
                            'id':image_id}
                    json_dict['images'].append(image)

                    for obj in self.get(root, 'object'):
                        category = self.get_and_check(obj, 'name', 1).text
                        if category not in categories:
                            new_id = len(categories) +1
                            categories[category] = new_id
                        category_id = categories[category]
                        bndbox = self.get_and_check(obj, 'robndbox', 1)
                        cx = float(self.get_and_check(bndbox, 'cx', 1).text)
                        cy = float(self.get_and_check(bndbox, 'cy', 1).text)
                        w = float(self.get_and_check(bndbox, 'w', 1).text)
                        h = float(self.get_and_check(bndbox, 'h', 1).text)
                        #angle = float(self.get_and_check(bndbox,'angle',1).text) 
                        
                        segmentation = self.get_and_check(obj,'segmentation',1)
                        x1 = float(self.get_and_check(segmentation,'x1',1).text)
                        y1 = float(self.get_and_check(segmentation,'y1',1).text)
                        x2 = float(self.get_and_check(segmentation,'x2',1).text)
                        y2 = float(self.get_and_check(segmentation,'y2',1).text)
                        x3 = float(self.get_and_check(segmentation,'x3',1).text)
                        y3 = float(self.get_and_check(segmentation,'y3',1).text)
                        x4 = float(self.get_and_check(segmentation,'x4',1).text)
                        y4 = float(self.get_and_check(segmentation,'y4',1).text)

                        ann = {'area': w*h, 'iscrowd': 0, 'image_id':
                            image_id, 'bbox':[cx, cy, w, h],
                            'category_id': category_id, 'id': bnd_id, 'ignore': 0,
                            'segmentation': [x1,y1,x2,y2,x3,y3,x4,y4]}
                        json_dict['annotations'].append(ann)
                        bnd_id = bnd_id + 1

                for cate, cid in categories.items():
                    cat = {'supercategory': 'none', 'id': cid, 'name': cate}
                    json_dict['categories'].append(cat)


                json_fp = open(save_json_path, 'w')
                json_str = json.dumps(json_dict,ensure_ascii=False, indent=4)
                json_fp.write(json_str)
                json_fp.close()
                print("Done")

