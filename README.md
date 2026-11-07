# Minecraft Custom Clouds

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/79b6ca95-bf86-4727-8506-8def63748a6c" />

nice sus gameplay lol are u kidding me

This repository contains a **ready-to-use Minecraft Resource Pack** and an **optional Python script** to instantly convert any image into a cloud shape.

---

## 🚀 1. How to Install and Play

1. Click the green **Code** button at the top of this page and select **Download ZIP**.
2. Open Minecraft and go to **Options** > **Resource Packs** > **Open Pack Folder**.
3. Move the downloaded `.zip` file into that folder.
4. In the game, move **Minecraft Custom Clouds** to the **Selected** column and click **Done**.

---

## 🎨 2. How to Create Custom Clouds

You can change the clouds using either the automatic script or by doing it manually.

### Option A: Automatic (Using the Python Script)
If you have an image (like a meme) and want to convert it automatically:
1. Put your image (e.g., `my_art.png`) in the main folder of this project.
2. Open your terminal/command prompt and run:
   ```bash
   python generate_clouds.py
   ```
3. Type the name of your image and press **Enter**. The script will automatically resize and place it in the correct game folder.

### Option B: Manual (Using an Image Editor)
1. Go to the folder: `assets/minecraft/textures/environment/`
2. Open `clouds.png` with any pixel art editor (like Photoshop, GIMP, Paint.NET, or Pixilart).
3. Draw your shape. **Every colored pixel will become a 3D cloud block in the sky.** Keep the background 100% transparent.
4. Save the file. Inside the game, press **`F3 + T`** to instantly reload the sky and see your changes!

---

## ⚙️ 3. Prerequisites & Dependencies

### For the Game (Resource Pack)
* **Minecraft Version:** Works on virtually **any version** of Minecraft Java Edition.
* **Important:** If the game says the pack is "Incompatible" (too old or too new), you can safely ignore the warning and turn it on anyway. It will still work!
* *(Optional)* If you want to fix the warning, open the `pack.mcmeta` file and change the `"pack_format"` number to match your version (e.g., `46` for Minecraft 1.21.4).

### For the Script (`generate_clouds.py`)
If you want to use the automatic Python script, you need:
1. **Python 3.x** installed on your computer.
2. The **Pillow** library (used for image processing). Install it by running:
   ```bash
   pip install Pillow
   ```

---

## 📄 License
