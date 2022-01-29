import cv2
import pandas as pd

imgPath = r'test_image.jpg'
img = cv2.imread(imgPath)

clicked = False
r = g = b = x_pos = y_pos = 0

index = ["color","colorName","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names = index, header = None)

def getColorName(R, G, B):
    minimum=10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"]))
        if d <= minimum:
            minimum = d
            color_name = csv.loc[i,"colorName"]
    return color_name


def draw_function(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global r,g,b,x_pos,y_pos,clicked
        clicked= True
        x_pos = x
        y_pos = y
        b,g,r = img[y,x,]
        b = int(b)
        g = int(g)
        r = int(r)

        """to debug x and y positions
        print(x_pos,y_pos)"""


cv2.namedWindow('image',)
cv2.setMouseCallback('image',draw_function)


while True:

    cv2.imshow('image',img)
    
    cv2.rectangle(img,(701,21),(905,62),(0,0,0),-1)
    cv2.putText(img,"Press Esc to exit",(705,46),5,0.8,(255,255,255),1,cv2.LINE_AA)
    if clicked:

        #cv2.rectangle(image,startpoint,endpoint,color,thickness)
        cv2.rectangle(img,(10,10),(600,50),(b,g,r),-1)

        # test string to get the color named
        text = getColorName(r,g,b) +" " + 'R=' + str(r) + " " + 'G=' + str(g) + " " + 'B=' + str(b)

        #cv2.putText(img,text,start,font(0-7),fontScale,fontcolor,thickness,lineType)
        cv2.putText(img,text,(40,40),3,0.7,(255,255,255),2,cv2.LINE_AA)

        if r + g + b >=600:
            cv2.putText(img,text,(40,40),3,0.7,(0,0,0),2,cv2.LINE_AA)
        
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break



cv2.destroyAllWindows()