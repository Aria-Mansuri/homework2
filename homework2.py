from PIL import Image

def zoom_image(image_path, zoom_factor):
    # Open the image
    img = Image.open(image_path)

    # Calculate the new size
    width, height = img.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    # Resize the image
    img_zoomed = img.resize((new_width, new_height), Image.LANCZOS)

    # Crop the center of the image
    left = (new_width - width) / 2
    top = (new_height - height) / 2
    right = (new_width + width) / 2
    bottom = (new_height + height) / 2

    img_cropped = img_zoomed.crop((left, top, right, bottom))

    return img_cropped

def main():
    image_path = input("Enter the path to the image: ")
    zoom_factor = float(input("Enter the zoom factor (e.g., 1.5 for 150%): "))

    # Zoom the image
    zoomed_image = zoom_image(image_path, zoom_factor)

    # Save the zoomed image
    output_path = "zoomed_image.png"
    zoomed_image.save(output_path)

    print(f"Zoomed image saved as {output_path}")

if __name__ == "__main__":
    main()







