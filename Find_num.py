from maix import camera,image,display,touchscreen,app,nn,time
from maix.network import wifi #导入WIFI模块
from maix import app, uart
import sys
from Usart import Usart1
from UI import UI



ts = touchscreen.TouchScreen()
ui1=UI()

detector = nn.YOLOv5(model="/root/models/yolov5s_num1.mud")
cam = camera.Camera(detector.input_width(), detector.input_height(), detector.input_format())
dis = display.Display()

def image_detect():
    t = time.time_ms()
    img = cam.read()
    
    # img=image.image2cv(img)
    # newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (320,224), 1, (320,224))  
    # img = cv2.undistort(img, mtx, dist, None, newcameramtx)
    # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # img=image.cv2image(img)
    # img=img.to_format(image.Format.FMT_RGB888) #转换图片格式为Format.FMT_RGB888
    
    objs = detector.detect(img, conf_th = 0.5, iou_th = 0.45)
    for obj in objs:
        img.draw_rect(obj.x, obj.y, obj.w, obj.h, color = image.COLOR_RED)
        msg = f'{detector.labels[obj.class_id]}: {obj.score:.2f}'
        img.draw_string(obj.x, obj.y, msg, color = image.COLOR_RED)
        
        # data = bytearray([0xF3,0xF4,int((obj.x+obj.w)/2),int((obj.y+obj.h)/2),obj.class_id,0xF5])
        # Usart1.write_str(data)
        print("x:{},y:{}, data: {}".format(int((obj.x+obj.w)/2), int((obj.y+obj.h)/2), obj.class_id))

        fps="fps: "+str(int(1000 / (time.time_ms() - t)))
        img.draw_string(0,200,fps,color = image.COLOR_RED, scale=2)
    dis.show(img)