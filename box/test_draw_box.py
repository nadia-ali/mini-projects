import pytest
from draw_box import draw_box

""" These tests are checking the output of the draw_box function given the height and width """

def test_4x4():
	assert draw_box(4,4) == '┌──┐\n│  │\n└──┘'

def test_6x6():
	assert draw_box(6,6) == '┌───┐\n│   │\n└───┘'

def test_8x8():
	assert draw_box(8,8) == '┌────┐\n│    │\n└────┘'

def test_10x10():
	assert draw_box(10,10) == '┌─────┐\n│     │\n└─────┘'
