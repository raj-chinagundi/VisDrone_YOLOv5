import os
from pathlib import Path
import PIL
from PIL import Image
  
# Get the list of all files and directories
# in the root directory
path1 = "/home/raj/Desktop/vizdrone/dataset/images/train/"
path2="/home/raj/Desktop/vizdrone/dataset/labels/train/"

dir_list = os.listdir(path1)
d2=os.listdir(path2)

for image in dir_list:
  img_path=str(path1+str(image))
  # print(img_path)
  img = PIL.Image.open(img_path)
  wx,hx=img.size
  temp="/home/raj/Desktop/vizdrone/dataset/labels/train/"+str(image)
  pstring=temp.replace('.jpg','.txt')
  file = Path(pstring)
  print(file)
  input_lines = file.read_text().split('\n')
  input_lines.pop();

  ouput_lines = []

  for input_line in input_lines:
              input_line = input_line.split(',')
              if int(input_line[4]):
                        x=int(input_line[0])
                        y=int(input_line[1])
                        w=int(input_line[2])
                        h=int(input_line[3])
                        xc=x+w/2
                        yc=y+h/2
                        xc/=wx
                        yc/=hx
                        w/=wx
                        h/=hx
                        ouput_lines.append(' '.join([input_line[5]]+[str(format(xc,".4f"))]+[str(format(yc,".4f"))]+[str(format(w,".4f"))]+[str(format(h,".4f"))]))

  file.write_text('\n'.join(ouput_lines))

















