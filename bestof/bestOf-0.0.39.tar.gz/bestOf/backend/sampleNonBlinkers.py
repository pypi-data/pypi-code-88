import os
import shutil


def main():
    lfw_path = '../resources/lfw/'
    dest_path = '../resources/blinkset/nonblinkers/'
    for folder_name in os.listdir(lfw_path):
        # sample only from people who have multiple images
        if len(list(os.listdir(lfw_path + str(folder_name) + '/'))) >= 2:
            images = os.listdir(lfw_path + str(folder_name))
            # sample the first image of that person
            shutil.copy(lfw_path + str(folder_name) +
                        '/' + str(images[0]), dest_path)


if __name__ == '__main__':
    main()
