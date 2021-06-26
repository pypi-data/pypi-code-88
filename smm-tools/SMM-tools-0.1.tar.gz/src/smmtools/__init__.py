from PIL import Image, ImageDraw, ImageFont
import textwrap    
import os

class  Instgaram:

    def text2carusel(text, font_type = "regular", indicator = True):
        #  setting a font
        package_directory = os.path.dirname(os.path.abspath(__file__))
        if font_type == "bold":
            font_path = os.path.join(package_directory, 'fonts', 'Roboto-Medium.ttf')
        else:
            font_path = os.path.join(package_directory, 'fonts', 'Roboto-Regular.ttf')
        # print(font_path)
        fnt = ImageFont.truetype(font_path, 40)

        article = text.split("\n")
        new_article = ""
        for paragraph in article:
            if len(paragraph)>45:
                paragraph = textwrap.fill(paragraph, 45)
                paragraph = "   " + paragraph
            new_article = new_article  + paragraph + "\n"

        lines = new_article.splitlines()
        total_page_count = int(len(lines)/16)+1
        images = []
        for line in range(total_page_count):
            page = "\n".join(lines[:16])
            lines = lines[16:]
            img = Image.new('RGB', (1080, 1080), color = (73, 109, 137))
            
            if indicator:
                indic = Image.new('RGB', (int(1080/total_page_count)*(line+1), 20), color = (250, 20, 20))  
                img.paste(indic) 
            d = ImageDraw.Draw(img)
            d.multiline_text((50,50), page, spacing=20, font=fnt, fill=(0, 0, 0))
            images.append(img)
            # img.save(str(line) + 'post.png')
        
        return images