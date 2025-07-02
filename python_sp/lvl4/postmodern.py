from PIL import Image, ImageDraw
import json


def draw_image(params_file, output_file):
    with open(params_file, 'r') as f:
        params_list = json.load(f)
    
    image_params = params_list[0]
    width = image_params['width']
    height = image_params['height']
    background = image_params['back']
    
    image = Image.new('RGB', (width, height), background)
    draw = ImageDraw.Draw(image)
    
    for param in params_list[1:]:
        shape = param['shape']
        xy = param['xy']
        fill = param.get('fill')
        outline = param.get('outline', None)
        width_param = param.get('width', 1)
        
        if shape == 'rectangle':
            draw.rectangle(xy, fill=fill, outline=outline, width=width_param)
        elif shape == 'ellipse':
            draw.ellipse(xy, fill=fill, outline=outline, width=width_param)
        elif shape == 'polygon':
            draw.polygon(xy, fill=fill, outline=outline)
        elif shape == 'line':
            draw.line(xy, fill=fill, width=width_param)
    
    image.save(output_file)


draw_image('params.json', 'image.png')