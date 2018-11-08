# This script contains 2 methods that each function very similar to one another to provide different results
# The major goal is extract metadata from images captured using dedicated cameras for use in scientific studies

import os
from PIL import Image, ExifTags
import argparse


# This method returns a dictionary of all meta data descriptors with the meta data associated to them
def extract_meta_data(image_path):
    if image_path is not None or image_path != '':
        img = Image.open(image_path)
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
        return exif
    else:
        return 0


# This method returns just a list of the meta data tags of an image. Doesn't return the associated meta
# data itself
def extract_meta_data_tags(image_path):
    if image_path is not None or image_path != '':
        img = Image.open(image_path)
        tags = [ExifTags.TAGS[k] for k, v in img._getexif().items() if k in ExifTags.TAGS]
        return tags
    else:
        return 0


if __name__ == '__main__':
    # Create an argparse object to get input from the command line
    parser = argparse.ArgumentParser('Input a JPG image file and extract meta data descriptors')
    # Then define the arguments from the command line
    # We have only one. The name of the file or the path of the file
    parser.add_argument("-f", "--file", help="Add the name of the file of which you want to "
                                             "see meta data descriptors", required=True)
    # Then we parse the arguments passed to us
    args = parser.parse_args()
    if args.file is not None:
        if os.path.exists(args.file):
            print('The path exists')
            meta_data_tags = extract_meta_data_tags(args.file)
            with open('meta_data_tags.txt', 'w') as tags_writer:
                for index, tag in enumerate(meta_data_tags, start=1):
                    tags_writer.write('{0}. {1}\n'.format(index, tag))
    else:
        print("You haven't given us anything here. Please try again")
