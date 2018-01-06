## Given a width(w) and a height(h), draw a box by size w by h.

## Version 1.0

Contents

1. Introduction to the program 
2. The logic behind the function
3. Tests 
4. Note

##1. This program includes a function named draw_box which takes two parameters: width(w) and height(h).The function contains variables which are assigned to ascii characters in order to make up the box. These were taken from https://en.wikipedia.org/wiki/Box-drawing_character. 


##2. The logic I used under the comment "box_math" in the function draw_box was: the top_left, top_right, bottom_left and bottom_right characters are constant regardless of which parameters are passed to the function. A box will always have four corners, so these stay the same. The changing parts of the box are the amount of horizontal and verical lines. A 4x4 box will have 2 vertical lines and 2 horizontal lines, so the width = w/2 and height = h/2. 

##3. I have used pytest to test the outputs of the draw_box function when passing 4x4, 6x6, 8x8 and 10x10. (https://docs.pytest.org/en/latest/getting-started.html)

##4. This may not be the best way to draw a box or test the function, so I am very happy to receive any feedback. Thank you 
