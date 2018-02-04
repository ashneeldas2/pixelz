all: 
	python makeimage.py

convert: image.ppm
	convert image.ppm image.png

clean: image.ppm
	rm image.ppm
	rm image.png
