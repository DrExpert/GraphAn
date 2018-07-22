#needs numpy, ffmpeg installed and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as math


_probe = 1072
_size = 16
_fps = 1
_time =1
_t0 = 1
_tn = 3

#here specify your function
def func(lenght, t):
    
    (x_min, x_max) = (-lenght, lenght)
    (y_min, y_max) = (-lenght, lenght)
    x, y = np.meshgrid(np.linspace(x_min, x_max, _probe),
                       np.linspace(y_min, y_max, _probe))
	
    Z = 20*np.power(np.power((np.mod(x,8)-4)*10,2)+np.power((np.mod(y,8)-4)*10,2),1/2)
    return Z.astype(dtype=np.int32)


	

def update(args):
    
    im.set_data(func(_size, args))
    return im,


if __name__ == '__main__':
    writer = animation.writers['ffmpeg']
	
	#you may want to change the artist part here
    writer = writer(fps=_fps, metadata=dict(artist='Anonymouse'))
    a = func(_size, 0)
    fig = plt.figure()
    plt.axis('off')
    
    im = plt.imshow(a, animated=True,cmap=plt.get_cmap('inferno'))
    ani = animation.FuncAnimation(fig, update, np.linspace(_t0, _tn, _time*_fps),
                                  interval=1)
    ani.save('2.mp4', writer=writer)