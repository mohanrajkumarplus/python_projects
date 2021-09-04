from PIL import Image, ImageFont, ImageDraw
import csv

title_font = ImageFont.truetype('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/Roboto-Medium.ttf',25)
title_font_large = ImageFont.truetype('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/Roboto-Medium.ttf',40)


with open('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/pathway_completion_details.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            poster_image = Image.open("C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/template_2.jpg")
            club_name = row[4]
            toastmaster_name = row[0]
            pathway_name = row[1]
            level_name = row[2]
            image_name_csv = row[3]
            print(image_name_csv)
            im = Image.open('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/' + image_name_csv )
            im = im.resize([210,290],Image.ANTIALIAS)
            im.save('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/' + 'resize_' + image_name_csv)
            im_resize = Image.open('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/' + 'resize_' + image_name_csv )
            poster_image.paste(im_resize,(642,254))
            image_editable = ImageDraw.Draw(poster_image)
            image_editable.text((28,43), club_name, (4, 13, 18), font=title_font_large)
            image_editable.text((185,270), level_name, (4, 13, 18), font=title_font)
            # only for Engaging Humor the text alignment is not good, so moving the pathway_name and toastmaster_name little to the right
            if pathway_name == 'Engaging Humor':
                image_editable.text((190,320), pathway_name, (4, 13, 18), font=title_font)
                image_editable.text((230,370), toastmaster_name, (4, 13, 18), font=title_font)
            else:
                image_editable.text((150,320), pathway_name, (4, 13, 18), font=title_font)
                image_editable.text((210,370), toastmaster_name, (4, 13, 18), font=title_font)
            image_name = 'poster_' + row[3]
            poster_image.save('C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/' + image_name )
            #Image.close("C:/Users/Mohan/AppData/Local/Programs/Python/Python39/pathway_completion_project/template.jpg")
            print('image saved')
            print(f'\t{row[0]} has completed {row[1]} pathway, of level {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


# reference - https://towardsdatascience.com/adding-text-on-image-using-python-2f5bf61bf448

# study
#
# Starting Coordinates: Pillow library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner.
# Text: String between single or double quotations
# Text color in RGB format: Google Picker is a great resource to find the best color. Search “Color Picker” on Google and it will show up.
# Font style: Google Fonts is a great resource to pick your font style, and you can also download the TTF(TrueType Font) file of the font family.
