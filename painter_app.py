import numpy as np 
import cv2 as cv  

# creating painter app using openCV:

# create an image / window :

colour_palette = np.zeros((150,256,3), np.uint8)
painter_img = np.zeros((600,1024,3), np.uint8)
painter_img[:] = [255,255,255]
cv.namedWindow('colour palette')
cv.namedWindow('painter')

# create trackbar for colour change:

def nothing(x):
	pass 

def brush(event, x, y, colour, thickness):

	global drawing, ix, iy, r, g, b, t

	if event == cv.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y
	elif event == cv.EVENT_MOUSEMOVE:
		if drawing == True:
			cv.circle(painter_img, (x,y), t, (b,g,r), -1)
	elif event == cv.EVENT_LBUTTONUP:
		drawing = False
		cv.circle(painter_img, (x,y), t, (b,g,r), -1)



cv.createTrackbar('R', 'colour palette', 0, 255, nothing)
cv.createTrackbar('G', 'colour palette', 0, 255, nothing)
cv.createTrackbar('B', 'colour palette', 0, 255, nothing)

# painter thickness:

cv.createTrackbar('thickness', 'colour palette', 0, 100, nothing)

# setting mouse event call back:

cv.setMouseCallback('painter',brush)

drawing = False # True if mouse is pressed 
mode = True # if True, draws rectangle else circle - toggled pressing m
ix,iy = -1,-1

while True:

	cv.imshow('colour palette',colour_palette)
	cv.imshow('painter', painter_img)
	k = cv.waitKey(1) & 0xFF
	# if event is esc, quit app
	if k == 27:
		break 
	# get current position of trackbars:
	r = cv.getTrackbarPos('R', 'colour palette')
	g = cv.getTrackbarPos('G', 'colour palette')
	b = cv.getTrackbarPos('B', 'colour palette')
	t = cv.getTrackbarPos('thickness', 'colour palette')

	colour_palette[:] = [b,g,r]



cv.destroyAllWindows()
