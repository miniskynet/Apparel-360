from flask import Flask, request, jsonify
import cv2
import numpy as np
from flask_cors import CORS
import pandas as pd
import json
import argparse
from tkinter import *
import os
app = Flask(__name__)
CORS(app)
@app.route("/generateColourPalattes", methods=['POST'])
def getColourPalatte():
  img_path = request.get_json(force=True)['rgbValues']
  print(img_path)
  r = img_path[0]
  g = img_path[1]
  b = img_path[2]

  #Creating argument parser to take image path from command line
  # ap = argparse.ArgumentParser()
  # ap.add_argument('-i', '--image', required=True, help="Image Path")
  # args = vars(ap.parse_args())
  # img_path = args['image']

  #Reading the image with opencv
  # img_path = request.file('image')
  # img_path.save(os.path.join(os.getcwd, 'static'), img_path.filename)
  # img = cv2.imread(os.path.join(os.getcwd, f'static/{img_path.filename}'))

  #declaring global variables (are used later on)
  # clicked = False
  # r = g = b = xpos = ypos = 0

  #Reading csv file with pandas and giving names to each column
  index=["color","color_name","hex","R","G","B"]
  csv = pd.read_csv('colors.csv', names=index, header=None)

  #function to calculate minimum distance from all colors and get the most matching color
  def getColorName(R,G,B):
       minimum = 10000
       for i in range(len(csv)):
           d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
           if(d<=minimum):
               minimum = d
               cname = csv.loc[i,"color_name"]
       return cname

  #function to get x,y coordinates of mouse double click
  # def draw_function(event, x,y,flags,param):
  #     if event == cv2.EVENT_LBUTTONDBLCLK:
  #         global b,g,r,xpos,ypos, clicked
  #         clicked = True
  #         xpos = x
  #         ypos = y
  #         b,g,r = img[y,x]
  #         b = int(b)
  #         g = int(g)
  #         r = int(r)
        
  # cv2.namedWindow('image')
  # cv2.setMouseCallback('image',draw_function)

  while(1):

      # cv2.imshow("image",img)
      # if (clicked):
    
          #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
          # cv2.rectangle(img,(20,20), (600,60), (b,g,r), -1)

          # #Creating text string to display( Color name and RGB values )
          text = getColorName(r,g,b) + ' [ '+'R='+ str(r) + '   '+ 'G='+ str(g) +'   '+ 'B='+ str(b)+' ] '
          print(text)
          
          # #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
          # cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

          # #For very light colours we will display text in black colour
          # if(r+g+b>=600):
          #     cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
              
          # clicked=False

          # #cv2.namedWindow('colors')
          
          # root = Tk()
          # root.title('rocommended colors')
          # root.geometry("600x600")

          # my_canvas= Canvas(root, width=400, height= 500, bg="white")

          #create rectangle
          if(r>=128 and r<=255) and (g>=0 and g<=160) and (b>=0 and b<=128):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=128 and r<=255) and (g>=169 and g<=255) and (b>=0 and b<=170):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="black" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "black" : "rgb(0, 0, 0)",
                  "navy" : "rgb(0, 32, 91)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})


          elif (r>=0 and r<=255) and (g>=79 and g<=255) and (b>=0 and b<=170):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=0 and r<=224) and (g>=0 and g<=255) and (b>=112 and b<=255):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="beige" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "beige" : "rgb(225, 198, 153)",
                  "black" : "rgb(0, 0, 0)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=72 and r<=186) and (g>=0 and g<=112) and (b>=128 and b<=238):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=199 and r<=255) and (g>=0 and g<=192) and (b>=133 and b<=255):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="beige" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "beige" : "rgb(225, 198, 153)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=245 and r<=255)and (g>=222 and g<=255) and (b>=179 and b<=224):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="brown" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                   "User selected" : text ,
                   "brown" : "rgb(161, 80, 19)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=139 and r<=244) and (g>=69 and g<=184) and (b>=19 and b<=143):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="beige" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="khaki" )

              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "beige" : "rgb(225, 198, 153)",
                  "navy" : "rgb(0, 32, 91)",
                  "khaki" : "rgb(255, 87, 51)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=245 and r<=255) and (g>=218 and g<=255) and (b>=173 and b<=250):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="navy" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="brown" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "navy" : "rgb(0, 32, 91)",
                  "brown" : "rgb(161, 80, 19)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=112 and r<=176) and (g>=128 and g<=196) and (b>=144 and b<=222):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r>=230 and r<=255) and (g>=230 and g<=255) and (b>=240 and b<=255):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="gray" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "grey" : "rgb(142, 142, 142)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==105 and g==105 and b==105):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==128 and g==128 and b==128):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==169 and g==169 and b==169):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="brown" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  "brown" : "rgb(161, 80, 19)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==192 and g==192 and b==192):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="navy" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="brown" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "navy" : "rgb(0, 32, 91)",
                  "brown" : "rgb(161, 80, 19)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==211 and g==211 and b==211):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==220 and g==220 and b==220):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==245 and g==245 and b==245):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="khaki" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="black" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="gray" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "khaki" : "rgb(255, 87, 51)",
                  "navy" : "rgb(0, 32, 91)",
                  "black" : "rgb(0, 0, 0)",
                  "grey" : "rgb(142, 142, 142)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==255 and g==255 and b==255):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="beige" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="navy" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="gray" )
            #   my_canvas.create_rectangle(50, 420, 300, 350, fill="black" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "beige" : "rgb(225, 198, 153)",
                  "navy" : "rgb(0, 32, 91)",
                  "grey" : "rgb(142, 142, 142)",
                  "black" : "rgb(0, 0, 0)",
                  }
            return jsonify({'Result':color_pallete})

          elif (r==0 and g==0 and b==0):
            #   my_canvas.create_rectangle(50, 120, 300, 50, fill="white" )
            #   my_canvas.create_rectangle(50, 220, 300, 150, fill="gray" )
            #   my_canvas.create_rectangle(50, 320, 300, 250, fill="navy" )
              
            #   my_canvas.pack(pady= 20)

            #   root.mainloop()
            color_pallete = {
                  "User selected" : text ,
                  "white" : "rgb(240, 240, 240)",
                  "grey" : "rgb(142, 142, 142)",
                  "navy" : "rgb(0, 32, 91)",
                  }
            return jsonify({'Result':color_pallete})

          else:
             color_pallete = {
                  "User selected" : text ,
                  "beige" : "rgb(225, 198, 153)",
                  "navy" : "rgb(0, 32, 91)",
                  "grey" : "rgb(142, 142, 142)",
                  "black" : "rgb(0, 0, 0)",
                  }
             return jsonify({'Result':color_pallete})
                  


          
        

      #Break the loop when user hits 'esc' key    
    #   if cv2.waitKey(20) & 0xFF ==27:
    #       break
      
#   cv2.destroyAllWindows()

if __name__ == "__main__":
  app.run(debug=TRUE)
