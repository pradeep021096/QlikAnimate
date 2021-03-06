import csv
import os
from PIL import Image

if __name__ == '__main__':
	
	#Input Folder Path
	inputfolder = "./input/SantaAndDeer"

	#For All images(40X25 = 1000 pixels) in Input Folder
	with open('output.csv', mode='a') as file:
		writer = csv.writer(file)
		frame = 0
		for filename in os.listdir(inputfolder):
			img = Image.open(os.path.join(inputfolder,filename))	#Open Image
			width, height = img.size
			img = img.convert('RGB')
			img = img.transpose(Image.FLIP_TOP_BOTTOM)				#To compensate (0,0) Data Read
			z=0
			
			# For all pixels in images
			for x in range(width):
				for y in range(height):
					z+=1						#Unique Dimension
					r,g,b = img.getpixel((x,y))	#Color Values
					data = [x,y,z,r,g,b,frame]	# X- Measure 1 , Y-Measure 2, Animator - Frame
					writer.writerow(data)
			frame +=1

