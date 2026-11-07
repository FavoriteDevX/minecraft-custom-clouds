import os
from PIL import Image

def convert_to_minecraft_clouds(input_image_path, output_size=(256, 256)):
    """
    Converts any input image into a functional Minecraft cloud texture map.
    Resizes the image and ensures the background is transparent.
    """
    # Target path inside the resource pack structure
    target_dir = os.path.join("assets", "minecraft", "textures", "environment")
    output_path = os.path.join(target_dir, "clouds.png")

    # Ensure the directory structure exists
    os.makedirs(target_dir, exist_ok=True)

    try:
        # Open the user's custom image
        with Image.open(input_image_path) as img:
            print(f"📦 Processing '{input_image_path}'...")
            
            # Convert image to RGBA to ensure transparency support
            rgba_img = img.convert("RGBA")
            
            # Resize image to Minecraft's standard cloud map resolution (256x256 or 512x512)
            # Using NEAREST neighbor to preserve crisp pixel-art edges
            resized_img = rgba_img.resize(output_size, Image.Resampling.NEAREST)
            
            # Save directly into the resource pack environment folder
            resized_img.save(output_path, "PNG")
            print(f"✨ Success! Custom clouds generated at: {output_path}")
            print("💡 Tip: Put the pack in your Minecraft folder and press F3+T in-game to reload!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_image_path}' was not found. Please check the path.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    print("--- Minecraft Cloud Generator Tool ---")
    user_file = input("Enter the filename/path of your custom image (e.g., amongus.png): ").strip()
    
    if user_file:
        convert_to_minecraft_clouds(user_file)
    else:
        print("❌ No file specified. Exiting.")
