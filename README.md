# Image-Compression
Image Compression using NumPy

This image compression algorithm uses NumPy to compress images without losing too much of the original image quality. We will use Singular Value Decomposition (SVD) as our compression technique. You can experiment with different compression ratios to compare the results.

Requirements:

Python 3.6 or later
NumPy
matplotlib
OpenCV
To install the required packages, run the following command:

pip install numpy matplotlib opencv-python-headless

Usage:

Run the script with the desired image file and compression ratio: python image_compression.py <image_file> <compression_ratio>
View the original and compressed images along with the compression statistics.


The image-compression.py provides an image compression algorithm using NumPy and Singular Value Decomposition (SVD). The compression ratio determines the number of singular values to retain, allowing you to balance the trade-off between image quality and compression. The script accepts an image file and a compression ratio as input, and it displays the original and compressed images along with the compression statistics.
