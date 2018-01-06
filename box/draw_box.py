def draw_box(w,h):
	""" This function takes two parameters width and height and returns a box of size w by h"""

	# ascii characters 
	top_left = '┌'
	top_right = '┐'
	horizontal_edge = '─'
	bottom_left = '└'
	bottom_right = '┘'
	vertical_edge = '│'

	# box math 
	width = int(w/2)
	height = int(h/2)
	# number of spaces to create the box 
	spaces = " " * width

	# creation of the box 
	top = top_left + (horizontal_edge * int(width)) + top_right

	for i in range(height):
		verticals = vertical_edge + spaces + vertical_edge

	bottom = bottom_left + horizontal_edge * int(width) + bottom_right

	box = top+ '\n' + verticals + '\n' + bottom

	return box 

def main():
	""" The main function is printing the output of the draw_box function"""
	print(draw_box(4,4))

if __name__ == '__main__':
	main()
