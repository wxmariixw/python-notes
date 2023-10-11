from PIL import ImageColor

def hex_string_to_RGB(hex_string): 
    rgb = ImageColor.getcolor(hex_string, "RGB")
    rgb_f = {'r': rgb[0], 'g': rgb[1], 'b': rgb[2]}
    return rgb_f