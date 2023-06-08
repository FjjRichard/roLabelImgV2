# roLabelImgV2

### 1.Installation

roLabelImgV2 is a graphical image annotation tool can label ROTATED rectangle regions, which is rewrite from 'roLabelImg'.

The original version 'roLabelImg''s link is here https://github.com/cgvict/roLabelImg.

### 2.New functions

1. **The<segmentation>tag is added to the XML file to save the rectangular coordinates**

2. **RoLabelImgV2 adds the function of one-button conversion of COCO format(Xml→Json)**

![image](https://github.com/richarddddd198/roLabelImgV2/blob/main/gui.PNG)

### 3.How to use

1. Refer to the introduction document of roLabelImg

2. Windows users can download and extract the **roLabelImgV2.zip** file and run it directly





### ↓↓↓↓↓↓↓↓↓Original document↓↓↓↓↓↓↓↓↓

# roLabelImg

roLabelImg is a graphical image annotation tool can label ROTATED
rectangle regions, which is rewrite from \'labelImg\'.

The original version \'labelImg\'\'s link is
here\<<https://github.com/tzutalin/labelImg>\>.

It is written in Python and uses Qt for its graphical interface.

[Watch a demo by author cgvict]{.title-ref}

![Demo Image](https://raw.githubusercontent.com/cgvict/roLabelImg/master/demo/demo4.png)

![image](https://raw.githubusercontent.com/cgvict/roLabelImg/master/demo/demo_v2.5.gif)

<https://youtu.be/7D5lvol_QRA>

Annotations are saved as XML files almost like PASCAL VOC format, the
format used by [ImageNet](http://www.image-net.org/).

## XML Format

```
<annotation verified="yes">
  <folder>hsrc</folder>
  <filename>100000001</filename>
  <path>/Users/haoyou/Library/Mobile Documents/com~apple~CloudDocs/OneDrive/hsrc/100000001.bmp</path>
  <source>
    <database>Unknown</database>
  </source>
  <size>
    <width>1166</width>
    <height>753</height>
    <depth>3</depth>
  </size>
  <segmented>0</segmented>
  <object>
    <type>bndbox</type>
    <name>ship</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
      <xmin>178</xmin>
      <ymin>246</ymin>
      <xmax>974</xmax>
      <ymax>504</ymax>
    </bndbox>
  </object>
  <object>
    <type>robndbox</type>
    <name>ship</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <robndbox>
      <cx>580.7887</cx>
      <cy>343.2913</cy>
      <w>775.0449</w>
      <h>170.2159</h>
      <angle>2.889813</angle>
    </robndbox>
    <segmentation>
      <x1>485.7773</x1>
      <y1>621.7875</y1>
      <x2>381.3207</x2>
      <y2>709.6281</y2>
      <x3>338.6755</x3>
      <y3>658.9161</y3>
      <x4>443.1321</x4>
      <y4>571.0755</y4>
    </segmentation>
  </object>
</annotation>
```

## Installation

### Download prebuilt binaries of original \'labelImg\'

- [Windows & Linux](http://tzutalin.github.io/labelImg/)
- OS X. Binaries for OS X are not yet available. Help would be
  appreciated. At present, it must be [built from source](#os-x).

### Build from source

Linux/Ubuntu/Mac requires at least [Python
2.6](http://www.python.org/getit/) and has been tested with [PyQt
4.8](http://www.riverbankcomputing.co.uk/software/pyqt/intro).

#### Ubuntu Linux

```
sudo apt-get install pyqt4-dev-tools
sudo pip install lxml
make all
./roLabelImg.py
./roLabelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

#### OS X

```
brew install qt qt4
brew install libxml2
make all
./roLabelImg.py
./roLabelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

#### Windows

Download and setup [Python 2.6 or
later](https://www.python.org/downloads/windows/),
[PyQt4](https://www.riverbankcomputing.com/software/pyqt/download) and
[install lxml](http://lxml.de/installation.html).

Open cmd and go to [roLabelImg](#roLabelimg) directory

```
pyrcc4 -o resources.py resources.qrc
python roLabelImg.py
python roLabelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

### Use Docker

```
docker pull tzutalin/py2qt4

docker run -it \
--user $(id -u) \
-e DISPLAY=unix$DISPLAY \
--workdir=$(pwd) \
--volume="/home/$USER:/home/$USER" \
--volume="/etc/group:/etc/group:ro" \
--volume="/etc/passwd:/etc/passwd:ro" \
--volume="/etc/shadow:/etc/shadow:ro" \
--volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
-v /tmp/.X11-unix:/tmp/.X11-unix \
tzutalin/py2qt4
```

You can pull the image which has all of the installed and required
dependencies.

## Usage

### Steps

1. Build and launch using the instructions above.
2. Click \'Change default saved annotation folder\' in Menu/File
3. Click \'Open Dir\'
4. Click \'Create RectBox\'
5. Click and release left mouse to select a region to annotate the rect
   box
6. You can use right mouse to drag the rect box to copy or move it

The annotation will be saved to the folder you specify.

You can refer to the below hotkeys to speed up your workflow.

### Create pre-defined classes

You can edit the
[data/predefined_classes.txt](https://github.com/tzutalin/labelImg/blob/master/data/predefined_classes.txt)
to load pre-defined classes

### Hotkeys

  ------------ --------------------------------------------

  Ctrl + u     Load all of the images from a directory

  Ctrl + r     Change the default annotation target dir

  Ctrl + s     Save

  Ctrl + d     Copy the current label and rect box

  Space        Flag the current image as verified

  w            Create a rect box

  e            Create a Rotated rect box

  d            Next image

  a            Previous image

  r            Hidden/Show Rotated Rect boxes

  n            Hidden/Show Normal Rect boxes

  del          Delete the selected rect box

  Ctrl++       Zoom in

  Ctrl\--      Zoom out

  ↑→↓←         Keyboard arrows to move selected rect box

  zxcv         Keyboard to rotate selected rect box

  ------------ --------------------------------------------

### How to contribute

Send a pull request

### License

[Free software: MIT
license](https://github.com/cgvict/roLabelImg/blob/master/LICENSE)

### Related

1. [ImageNet Utils](https://github.com/tzutalin/ImageNet_Utils) to
   download image, create a label text for machine learning, etc
2. [Docker hub to run it](https://hub.docker.com/r/tzutalin/py2qt4)
