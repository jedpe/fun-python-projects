# Chaos game

The chaos game was first described by Michael Barnsley in 1988 on his textbook "Fractals Everywhere". The game can be played as follows:

1. Draw three points, each on the vertices of a triangle.
2. Select a random starting point inside the triangle.
3. Throw a die to choose one of the vertices at random.
4. Move half the distance between the current point and the chosen vertex aand draw another point there.
5. Repeat steps 3 and 4 as many times as possible.

The video by [Numberphile](https://www.youtube.com/watch?v=kbKtFN71Lfs&t=200s&ab_channel=Numberphile) gives a more detailed explanation about the Sierpiński gasket and the chaos game.

This implementation used the Turtle graphics library.

## Sierpinski gasket

The Sierpiński gasket, also known as Sierpiński triangle, is a fractal with the shape of a triangle subdivided into smaller triangles. This code will produce the following triangle using the Turtle library:

![Sierpiński gasket](https://github.com/jedpe/fun-python-projects/blob/master/chaos_game/imgs/triangle.jpg)

To save the image

```python
import os
from PIL import Image

s = turtle.getscreen()
img = s.getcanvas().postscript(file='temp_img.eps')
img.save("sierpinski_triangle.jpg")
os.remove('temp_img.eps')
```
