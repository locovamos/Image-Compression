import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

def compress_image(image, compression_ratio):
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    U, S, V = np.linalg.svd(gray_image, full_matrices=False)

    singular_values_to_keep = int(compression_ratio * len(S))

    U_reduced = U[:, :singular_values_to_keep]
    S_reduced = np.diag(S[:singular_values_to_keep])
    V_reduced = V[:singular_values_to_keep, :]

    compressed_image = np.dot(U_reduced, np.dot(S_reduced, V_reduced))

    return compressed_image

def main(image_file, compression_ratio):
    # Load the image
    image = cv2.imread(image_file)

    if image is None:
        print("Error: Unable to load image.")
        sys.exit(1)

    compressed_image = compress_image(image, compression_ratio)

    original_size = image.size
    compressed_size = compressed_image.size
    compression_percentage = (1 - compressed_size / original_size) * 100

    plt.figure(figsize=(12, 6))

    plt.subplot(121)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(122)
    plt.title("Compressed Image")
    plt.imshow(compressed_image, cmap="gray")
    plt.axis("off")

    plt.suptitle(f"Compression Ratio: {compression_ratio}, "
                 f"Compression: {compression_percentage:.2f}%")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_compression.py <image_file> <compression_ratio>")
        sys.exit(1)

    image_file = sys.argv[1]
    compression_ratio = float(sys.argv[2])

    main(image_file, compression_ratio)
