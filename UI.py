from maix import image,app,time


blobs_mode=False






exit_label1 = "LI"
exit_label2 = "LA"
exit_label3 = "AI"
exit_label4 = "AA"
exit_label5 = "BI"
exit_label6 = "BA"
exit_label7 = "+"
exit_label8 = "-"
exit_label9 = "MD"

L1 = image.load("/root/photo/LI.png")
L2 = image.load("/root/photo/LA.png")
A1 = image.load("/root/photo/AI.png")
A2 = image.load("/root/photo/AA.png")
B1 = image.load("/root/photo/BI.png")
B2 = image.load("/root/photo/BA.png")
O1 = image.load("/root/photo/+.png")
O2 = image.load("/root/photo/-.png")
Ex = image.load("/root/photo/ret.png")

size1 = image.string_size(exit_label1)
size2 = image.string_size(exit_label2)
size3 = image.string_size(exit_label3)
size4 = image.string_size(exit_label4)
size5 = image.string_size(exit_label5)
size6 = image.string_size(exit_label6)
size7 = image.string_size(exit_label7)
size8 = image.string_size(exit_label8)
size9 = image.string_size(exit_label9)

Ex1 = [0, 0, 8*2 + size1.width(), 12 * 2 + size1.height()]

Lmin1 = [0, 192, 8*2+size1.width(), 12 * 2 + size1.height()]
Lmax2 = [31, 192,8*2+size2.width(), 12 * 2 + size2.height()]
Amin3 = [64, 192,8*2+ size3.width(), 12 * 2 + size3.height()]
Amax4 = [95, 192, 8*2+size4.width(), 12 * 2 + size4.height()]
Bmin5 = [130, 192, 8*2+size5.width(), 12 * 2 + size5.height()]
Bmax6 = [162, 192,8*2+ size6.width(), 12 * 2 + size6.height()]
Odd7 = [196, 192, 8*2+size7.width(), 12 * 2 + size7.height()]
Odd8 = [227, 192, 8*2+size8.width(), 12 * 2 + size8.height()]
Blob = [260, 192, 8*2+size8.width(), 12 * 2 + size8.height()]

touch_flag=0
#640,480？

    
class UI:
    x1=0
    y1=0
    
    Lmin=0
    Lmax=36
    Amin=-19
    Amax=50
    Bmin=-7
    Bmax=25
    odd=10
    
    def UI1(self,img0):
        
        img=img0
        img.draw_image(0, 0, Ex)
        
        # img.draw_image(0, 192, L1)
        # img.draw_image(31, 192, L2)
        # img.draw_image(64, 192, A1)
        # img.draw_image(95, 192, A2)
        # img.draw_image(130, 192, B1)
        # img.draw_image(160, 192, B2)
        # img.draw_image(192, 192, O1)
        # img.draw_image(227, 192, O2)
        
        
        img.draw_string(8, 200, exit_label1,image.COLOR_WHITE)
        img.draw_string(31+8, 200, exit_label2, image.COLOR_WHITE)
        img.draw_string(64+8,200, exit_label3, image.COLOR_WHITE)
        img.draw_string(95+8, 200, exit_label4, image.COLOR_WHITE)
        img.draw_string(130+8, 200, exit_label5, image.COLOR_WHITE)
        img.draw_string(162+8, 200, exit_label6, image.COLOR_WHITE)
        img.draw_string(196+8, 200, exit_label7, image.COLOR_WHITE)
        img.draw_string(227+8, 200, exit_label8, image.COLOR_WHITE) 
        img.draw_string(260+8, 200, exit_label9, image.COLOR_WHITE) 
        
        
        # img.draw_string(31+8, 150,str(Lmax), image.COLOR_RED)
        # img.draw_string(64+8,150, str(Amin), image.COLOR_RED)
        # img.draw_string(95+8,150, str(Amax), image.COLOR_RED)
        # img.draw_string(130+8,150,str(Bmin), image.COLOR_RED)
        # img.draw_string(162+8,150,str(Bmax), image.COLOR_RED)
        # img.draw_string(196+8,150,str(odd) , image.COLOR_RED)
         
              
        img.draw_rect(Lmin1[0], Lmin1[1], Lmin1[2], Lmin1[3],  image.COLOR_WHITE, 2)
        img.draw_rect(Lmax2[0], Lmax2[1], Lmax2[2], Lmax2[3],  image.COLOR_WHITE, 2)
        img.draw_rect(Amin3[0], Amin3[1], Amin3[2], Amin3[3],  image.COLOR_WHITE, 2)
        img.draw_rect(Amax4[0], Amax4[1], Amax4[2], Amax4[3],  image.COLOR_WHITE, 2)
        img.draw_rect(Bmin5[0], Bmin5[1], Bmin5[2], Bmin5[3],  image.COLOR_WHITE, 2)
        img.draw_rect(Bmax6[0], Bmax6[1], Bmax6[2], Bmax6[3],  image.COLOR_WHITE, 2)        
        img.draw_rect(Odd7[0], Odd7[1], Odd7[2], Odd7[3],  image.COLOR_WHITE, 2) 
        img.draw_rect(Odd8[0], Odd8[1], Odd8[2], Odd8[3],  image.COLOR_WHITE, 2)
        img.draw_rect(Blob[0], Blob[1], Blob[2], Blob[3],  image.COLOR_WHITE, 2)
             
    def is_in_button(self,x, y, btn_pos):
        
        return x > btn_pos[0] and x < btn_pos[0] + btn_pos[2] and y > btn_pos[1] and y < btn_pos[1] + btn_pos[3]
    
    
    def parameter_ui(self,Lmin,Lmax,Amin,Amax,Bmin,Bmax,ts,img,dis):
        click = True
        x, y, pressed = ts.read()
        x, y = image.resize_map_pos_reverse(img.width(), img.height(), dis.width(), dis.height(), image.Fit.FIT_CONTAIN, x, y)
        if self.is_in_button(x, y, Lmin1) and self.x1!=x and self.y1!=y:
            self.Lmin+=self.odd
            self.x1=x
            self.y1=y
            print(Lmin)
        
            while ts.read()[2]:
                time.sleep(0.1)
        if self.is_in_button(x, y, Lmax2) and self.x1!=x and self.y1!=y:        
            self.Lmax+=self.odd
            self.x1=x
            self.y1=y
            print(self.Lmax)
            while ts.read()[2]:
                time.sleep(0.1)
            
        if self.is_in_button(x, y, Amin3) and self.x1!=x and self.y1!=y:
            self.Amin+=self.odd
            self.x1=x
            self.y1=y
            print(self.Amin)
            while ts.read()[2]:
                time.sleep(0.1)
        if self.is_in_button(x, y, Amax4) and self.x1!=x and self.y1!=y:
            self.Amax+=self.odd
            self.x1=x
            self.y1=y
            print(self.Amax)
            while ts.read()[2]:
                time.sleep(0.1)
        if self.is_in_button(x, y, Bmin5) and self.x1!=x and self.y1!=y:
            self.Bmin+=self.odd
            self.x1=x
            self.y1=y
            print(self.Bmin)
            while ts.read()[2]:
                time.sleep(0.1)
        if self.is_in_button(x, y, Bmax6) and self.x1!=x and self.y1!=y:
            self.Bmax+=self.odd
            self.x1=x
            self.y1=y
            print(self.Bmax)
            while ts.read()[2]:
                time.sleep(0.1)    
        if self.is_in_button(x, y, Odd7) and self.x1!=x and self.y1!=y:
            self.odd+=1
            self.x1=x
            self.y1=y
            print(self.odd)
            while ts.read()[2]:
                time.sleep(0.1)
        if self.is_in_button(x, y, Odd8) and self.x1!=x and self.y1!=y:
            self.odd-=1
            self.x1=x
            self.y1=y
            print(self.odd)
            while ts.read()[2]:
                time.sleep(0.1) 
        if self.is_in_button(x, y, Blob) and self.x1!=x and self.y1!=y:
            blobs_mode = not blobs_mode
            print(blobs_mode)
            while ts.read()[2]:
                time.sleep(0.1)
                         
        if self.is_in_button(x, y, Ex1):
            app.set_exit_flag(True)
            
        else:
            slide = False
            click = not tp[2]