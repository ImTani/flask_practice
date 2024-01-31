from PIL import Image


primary_colour = "F8F0E5"
secondary_colour = "102C57"


def replace_white_pixels(input_path, output_path, new_color_hex):

    img = Image.open(input_path)

    new_color_rgb = tuple(int(new_color_hex[i:i+2], 16) for i in (0, 2, 4))

    img_data = img.getdata()

    # Replace white pixels, considering transparency
    new_img_data = [
        new_color_rgb + (pixel[3],) if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255 else pixel
        for pixel in img_data
    ]

    new_img = Image.new('RGBA' if img.mode == 'RGBA' else 'RGB', img.size)
    new_img.putdata(new_img_data)

    new_img.save(output_path)

def update_images():
    replace_white_pixels("app/static/assets/user_icon_base.png", "app/static/assets/user_icon.png", primary_colour)
    replace_white_pixels("app/static/assets/home_icon_base.png", "app/static/assets/home_icon.png", secondary_colour)