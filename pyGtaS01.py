# encoding: utf-8

import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time 

last_time = time.time()
while(True):
    # captura tela
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    
    # dimensao da tela a ser capturada
    print("Loop took {} seconds".format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



