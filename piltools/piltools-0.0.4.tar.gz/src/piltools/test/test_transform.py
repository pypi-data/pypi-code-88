# Standard Library
import unittest

# Third Party
from PIL import Image

# Local
from piltools.transform import ar_resize, recrop

TEST_IMAGE_PATH = "src/piltools/test/cosmos.png"
TEST_IMAGE = Image.open(TEST_IMAGE_PATH)

class TestTransform(unittest.TestCase):


    def test_ar_resize(self):
        width, height = TEST_IMAGE.size
        resized = ar_resize(TEST_IMAGE, 2)
        new_width, new_height = resized.size
        self.assertEqual(width*2, new_width)
        self.assertEqual(height*2, new_height)


    def test_recrop(self):
        width, height = TEST_IMAGE.size

        v_opts = ["top", "center", "bottom"]
        h_opts = ["left", "center", "right"]

        for v_opt in v_opts:
            for h_opt in h_opts:
                # Upscaling
                recropped = recrop(
                    TEST_IMAGE,
                    (width*2, height*3),
                    v_align=v_opt,
                    h_align=h_opt
                )
                new_width, new_height = recropped.size
                self.assertEqual(new_width, width*2)
                self.assertEqual(new_height, height*3)
                # recropped.show()

                # Downscaling
                recropped = recrop(
                    TEST_IMAGE,
                    (width/2, height/4),
                    v_align=v_opt,
                    h_align=h_opt
                )
                new_width, new_height = recropped.size
                self.assertEqual(new_width, width/2)
                self.assertEqual(new_height, height/4)
                # recropped.show()            
        

if __name__ == "__main__":
    unittest.main()
