import pygame as pg
import pygame.camera as pgcam
from pygame.locals import *
import test_cameraControl as cc

pg.init()
pgcam.init()

camlist = pgcam.list_cameras()
for c in camlist:
    print(c)


cc.ms=0.5
# cam = pgcam.Camera("/dev/video0",(640,480))
# print(cam)
# cam.start()
# print(cam.get_size())
# print(cam.get_controls())

# raw = cam.get_raw()
# print(len(raw))
# print(raw[0:100])

class Capture(object):
    def __init__(self):
        self.size = (640,480)
        # create a display surface. standard pygame stuff
        self.display = pg.display.set_mode(self.size, 0)

        # this is the same as what we saw before
        self.clist = pgcam.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pgcam.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pg.surface.Surface(self.size, 0, self.display)

    def camera_control(self, pressedKeys):
        if pressedKeys:
            if pressedKeys[pg.K_UP]:
                cc.moveUp()
            if pressedKeys[pg.K_DOWN]:
                cc.moveDown()
            if pressedKeys[pg.K_LEFT]:
                cc.moveLeft()
            if pressedKeys[pg.K_RIGHT]:
                cc.moveRigth()

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0,0))
        pg.display.flip()

    def main(self):
        going = True
        #posicion camara
        pan = ''
        tilt=''
        clock = pg.time.Clock()
        while going:
            events = pg.event.get()
            for event in events:
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False

            self.camera_control(pg.key.get_pressed() )
            self.get_and_flip()
            
            clock.tick(30)


cp = Capture()
cp.main()