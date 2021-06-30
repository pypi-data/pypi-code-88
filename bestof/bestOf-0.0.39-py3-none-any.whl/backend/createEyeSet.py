import os
import identifyPeople


def main():
    blinkset_path = '../resources/blinkset/'
    eyeset_path = '../resources/eyeset_colored/'
    for folder_name in os.listdir(blinkset_path):

        # use the following code block when only updating one class, comment out pass or continue as apt
        if folder_name == 'blinkers':
            continue
            # pass
        else:
            # continue
            pass

        for img_name in os.listdir(blinkset_path + folder_name + '/'):
            try:
                eyes_gen = identifyPeople.get_eye_frame_from_img(
                    blinkset_path + folder_name + '/' + img_name)
                eyes = None
                for eye_box in eyes_gen:
                    eyes = eye_box
                    break
                if not eyes:
                    continue
                image = identifyPeople.read_img(
                    blinkset_path + folder_name + '/' + img_name)
                image = image[eyes[0][1]:eyes[1][1], eyes[0][0]:eyes[1][0]]
                identifyPeople.save_img_colored(
                    eyeset_path + folder_name + '/' + img_name, image)
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    main()
