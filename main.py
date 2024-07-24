from maix import camera,image,display,touchscreen,app,nn,time
from maix.network import wifi #导入WIFI模块
from maix import app, uart
import sys
from Usart import Usart1
from UI import UI,blobs_mode



ts = touchscreen.TouchScreen()

ui1=UI()

# cam = camera.Camera(320, 240, image.Format.FMT_GRAYSCALE)
cam =camera.Camera(320, 240)
dis = display.Display()

#usart
# ports = uart.list_devices()

# serial0 = uart.UART(ports[0], 115200)
# serial0.write("hello 1\r\n".encode())
# serial0.write_str("hello 2\r\n")


USART1_REC_LEN = 200
USART1_RX_BUF = [0] * 10
USART1_RX_STA = 0
USART1_NewData = None
RxState1 = 0
mubiao_x = None
mubiao_BF = None


#x y w h 
roi = [40, 0, 220, 224]
area_threshold = 1000
pixels_threshold = 1000
thresholds = [[ui1.Lmin, ui1.Lmax, ui1.Amin, ui1.Amax, ui1.Bmin, ui1.Bmax]]
invert = False
x_stride = 2
y_stride = 1
merge = True
margin = 10
x_hist_bins_max = 0
y_hist_bins_max = 1

white_thresholds=[[96, 100, -13, 5, -11, 18]]
# thresholds = ((0, 100, 20, 80, 10, 80),)
# img = img = src_img.copy()
# new_img = img.binary(thresholds, zero = True, mask = mask_img, copy = True)
# img.save("out/out_binary_zero_copy_src.jpg")
# new_img.save("out/out_binary_zero_copy.jpg")


max_num_x = 0
max_num_y = 0
max_num_w = 0
max_num_h = 0

time_red=0
time_black=0
time_green=0
def find_max(max_num,num):
    
    
    if num > max_num:
        max_num = num
     
        return max_num
    else:
        return max_num
def read_and_correct_image(cam, strength=1.8, zoom=1.0, x_corr=0.0, y_corr=0.0):
    img = cam.read()
    return img.lens_corr(strength=strength, zoom=zoom, x_corr=x_corr, y_corr=y_corr)



def find_blobs():
    t = time.time_ms()
    img = cam.read()
    parameter = ui1.Lmin, ui1.Lmax, ui1.Amin, ui1.Amax, ui1.Bmin, ui1.Bmax,ui1.odd
    thresholds = [[ui1.Lmin, ui1.Lmax, ui1.Amin, ui1.Amax, ui1.Bmin, ui1.Bmax]]
    
    
    # img=img.lens_corr(strength = 1.8,  zoom = 1.0,  x_corr = 0.0, y_corr = 0.0)
    if blobs_mode:
        blobs = img.find_blobs(thresholds, invert, roi, x_stride, y_stride, area_threshold, pixels_threshold, merge, margin, x_hist_bins_max, y_hist_bins_max)
    else:
        blobs = img.find_blobs(white_thresholds, invert, x_stride, y_stride, area_threshold, pixels_threshold, merge, margin, x_hist_bins_max, y_hist_bins_max)
    
    ui1.UI1(img)
    ui1.parameter_ui(ui1.Lmin,ui1.Lmax,ui1.Amin,ui1.Amax,ui1.Bmin,ui1.Bmax,ts,img,dis)
    
    img.draw_string(8, 150,   str(parameter), image.COLOR_RED) 
    
    for a in blobs:
        rect = a.rect()
        img.draw_rect(rect[0], rect[1], rect[2], rect[3], image.COLOR_GREEN)
        print("x:{},y:{}".format(int((rect[0]+rect[2])/2), int((rect[1]+rect[3])/2)))
        fps="fps: "+str(int(1000 / (time.time_ms() - t)))
        img.draw_string(250,0,fps,color = image.COLOR_RED, scale=1.5)
        
        data = bytearray([0x3B,0x3C,rect[0],rect[1],rect[2],rect[3],0x25])
        Usart1.serial.write_str(data)       
    dis.show(img)
    





# 使用示例


#找最大色块怎么写？
while not app.need_exit():
    
    find_blobs()

    # img = read_and_correct_image(cam)
    # img0 = read_and_correct_image(cam)
    # img1 = read_and_correct_image(cam)
    
    # Lmin=0
    # Lmax=36
    # Amin=-19
    # Amax=50
    # Bmin=-7
    # Bmax=25
    
    # thresholds_black= [[0, 17, -127, 128, -127, 128]]
    # thresholds_red=   [[0,100, 21, 127, -30, 5]]
    # thresholds_green= [[0, 100, -16, -128, -128, 127]]
    # thresholds_white=  [[63, 83, -12, 8, -14, 6]]    
    
    # # blobs_black = img.find_blobs(thresholds_black, invert, roi, x_stride, y_stride,1000,1000 ,merge, margin, x_hist_bins_max, y_hist_bins_max)
    # blobs_red = img0.binary(thresholds_red, zero = False,invert=False).find_blobs(white_thresholds, invert, roi, x_stride, y_stride,1,1   ,merge, margin, x_hist_bins_max, y_hist_bins_max)
    # blobs_green =img1.binary(thresholds_green, zero = False,invert=False).find_blobs(white_thresholds, invert, roi, x_stride, y_stride,5,5   ,merge, margin, x_hist_bins_max, y_hist_bins_max)
    
    # img.draw_rect(40, 0, 220, 224, image.COLOR_RED)
    
    
    # # if blobs_black :    
        
        
       
    # #     for a in blobs_black:
    # #         corners = a.corners()
    # #         time_black=time_black+1
    # #         for i in range(4):
    # #             img.draw_line(corners[i][0], corners[i][1], corners[(i + 1) % 4][0], corners[(i + 1) % 4][1], image.COLOR_RED)
                
    # #             img.draw_string(corners[0][0] + 5, corners[0][1] + 5, "corners area: " + str(a.area()), image.COLOR_RED)
        
              
            
            
    # #         # max_num_x = find_max(max_num_x, corners[i][0])
    # #         # max_num_y = find_max(max_num_y, corners[i][1])
    # #         # max_num_w = find_max(max_num_w, corners[(i + 1) % 4][0])
    # #         # max_num_h = find_max(max_num_h, corners[(i + 1) % 4][1])

    # #         x1, y1 = corners[0]
    # #         x2, y2 = corners[1]
    # #         x3, y3 = corners[2]
    # #         x4, y4 = corners[3]
            
    # #         x1 = x1 % 256
    # #         y1 = y1 % 256
    # #         x2 = x2 % 256
    # #         y2 = y2 % 256
    # #         x3 = x3 % 256
    # #         y3 = y3 % 256
    # #         x4 = x4 % 256
    # #         y4 = y4 % 256
    # #         if time_black>13 :
    # #             print(corners)
    # #             data1 = bytearray([0x1A, 0x2B,x1, y1, x2, y2,x3,y3,x4,y4,0x3C])
    # #             Usart1.serial.write_str(data1)
    # #             time_black=0
                
 


    
    # if blobs_red :
    #     time_red=time_red+1 
    #     for b in blobs_red :
    #         rect_red = b.rect()
    #         img.draw_rect(rect_red[0], rect_red[1], rect_red[2], rect_red[3], image.COLOR_RED)
    #         if time_red>4:
    #             print("red:x:{},y:{}".format(int((rect_red[0]+rect_red[2])/2), int((rect_red[1]+rect_red[3])/2)))     
    #             data2 = bytearray([0x2B,0x2C,int((rect_red[0]+rect_red[2])/2),int((rect_red[1]+rect_red[3])/2),0x25])
    #             Usart1.serial.write_str(data2)
    #             time_red=0
            
    # if blobs_green:
    #     time_green=time_green+1    
    #     for c in blobs_green :
    #         rect_green = c.rect()
    #         img.draw_rect(rect_green[0], rect_green[1], rect_green[2], rect_green[3], image.COLOR_GREEN)
    #         if time_green>3:
                
    #             print("green:x:{},y:{}".format(int((rect_green[0]+rect_green[2])/2), int((rect_green[1]+rect_green[3])/2)))
    #             data3 = bytearray([0x3A,0x4C,int((rect_green[0]+rect_green[2])/2),int((rect_green[1]+rect_green[3])/2),0x5D])
    #             Usart1.serial.write_str(data3)
    #             time_green=0        
        
               
    # dis.show(img)


