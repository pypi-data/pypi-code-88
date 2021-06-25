import math
import matplotlib.pyplot as plt
import pyregion
import matplotlib.pyplot as plt
# from demo_helper import show_region

def demo_header():
    from astropy.io.fits import Header
    return Header.fromtextfile("sample_fits01.header")

region_list = [
    "test01_fk5_sexagecimal.reg",
    "test01_gal.reg",
    "test01_img.reg",
    "test01_ds9_physical.reg",
    "test01_fk5_degree.reg",
    "test01_mixed.reg",
    "test01_ciao.reg",
    "test01_ciao_physical.reg",
]

fig, ax = plt.subplots(1, num=1, clear=True)
h = demo_header()
reg_name = "test01_ciao.reg"
r = pyregion.open(reg_name).as_imagecoord(h)

patch_list, text_list = r.get_mpl_patches_texts()
for p in patch_list:
    ax.add_patch(p)
for t in text_list:
    ax.add_artist(t)
# patch_list[0].set_facecolor(None)

# ax_list = show_region(fig, region_list)
# for ax in ax_list:
ax.set_xlim(596, 1075)
ax.set_ylim(585, 1057)
