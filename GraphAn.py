#needs numpy, ffmpeg installed and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as math

resolution = 3000
size = 2400


#here specify your function
def func(lenght, t):
    
    (x_min, x_max) = (-lenght, lenght)
    (y_min, y_max) = (-lenght, lenght)
    X, Y = np.meshgrid(np.linspace(x_min, x_max, lenght/2),
                       np.linspace(y_min, y_max, lenght/2))
	
    Z = 5*np.sin((x)*np.sin(y)*np.sin(y*x+(t/10)))
    return Z.astype(dtype=np.int32)


	

def update(args):
    
    im.set_data(func(size, args))
    return im,


if __name__ == '__main__':
    writer = animation.writers['ffmpeg']
	
	#you may want to change the artist part here
    writer = writer(fps=15, metadata=dict(artist='Anonymouse'), bitrate=80000)
    a = func(size, 0)
    fig = plt.figure()
    plt.axis('off')
    
    im = plt.imshow(a, animated=True)
    ani = animation.FuncAnimation(fig, update, np.arange(1, 200),
                                  interval=1)
    ani.save('generated.mp4', writer=writer)