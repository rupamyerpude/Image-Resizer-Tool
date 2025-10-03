import os
from PIL import Image

def batch_resize_images(input_folder, output_folder, target_width, target_height):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                # Convert to RGB if needed (avoids issues with PNG transparency)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Resize image
                resized_img = img.resize((target_width, target_height), Image.LANCZOS)

                # Save resized image
                resized_img.save(output_path)
                print(f"✅ Resized and saved: {filename}")
        except Exception as e:
            print(f"⚠️ Skipping {filename}: {e}")


if __name__ == "__main__":
    # 🔧 User configuration
    input_folder = r"C:\Users\Rupam\OneDrive\Attachments\Documents\Internship.py\images"       # folder with original images
    output_folder = r"C:\Users\Rupam\OneDrive\Attachments\Documents\Internship.py\resizeimages"  # folder to save resized images
    target_width = 800
    target_height = 600

    batch_resize_images(input_folder, output_folder, target_width, target_height)
