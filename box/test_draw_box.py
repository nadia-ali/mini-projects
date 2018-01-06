import pytest
from draw_box import draw_box

""" These tests are checking the length of the height and width of the boxes """

def test_4x4():
	""" This function is testing the input height 4 is now a height of 2 """
	assert draw_box(4,4) == '┌──┐\n│  │\n└──┘'

def test_6x6():
	""" This function is testing the input width 8 is now a width of 4 """
	assert draw_box(6,6) == '┌───┐\n│   │\n└───┘'

def test_8x8():
	""" This function is testing the input height 4 is now a height of 2 """
	assert draw_box(8,8) == '┌────┐\n│    │\n└────┘'

def test_10x10():
	""" This function is testing the input height 4 is now a height of 2 """
	assert draw_box(10,10) == '┌─────┐\n│     │\n└─────┘'
