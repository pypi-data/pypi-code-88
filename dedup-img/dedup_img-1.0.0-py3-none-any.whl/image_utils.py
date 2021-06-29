from PIL import Image
import os


def get_size(file):
    # 获取文件大小: kb
    size = os.path.getsize(file)
    return size / 1024


def get_outfile(infile, outfile):
    if outfile:
        return outfile
    pth, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(pth, suffix)
    return outfile


def compress_image(infile, outfile='', mb=150, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
        :param infile: 压缩源文件
        :param outfile: 压缩文件保存地址
        :param mb: 压缩目标，KB
        :param step: 每次调整的压缩比率
        :param quality: 初始压缩比率
        :return: 压缩文件地址，压缩文件大小
        """
    outfile = get_outfile(infile, outfile)
    o_size = get_size(infile)
    if o_size <= mb:
        im = Image.open(infile)
        im.save(outfile)
    else:
        while o_size > mb:
            im = Image.open(infile)
            im.save(outfile, quality=quality)
            if quality - step < 0:
                break
            quality -= step
            o_size = get_size(outfile)
    return outfile, get_size(outfile)


def create_thumbnail(infile, size=(200, 200)):
    root, filename = os.path.split(infile)
    thumbnail_dir = os.path.join(root, 'thumbnail')
    if not os.path.exists(thumbnail_dir):
        os.mkdir(thumbnail_dir)
    outfile = os.path.join(thumbnail_dir, filename)

    if not os.path.exists(outfile):
        img = Image.open(infile)
        img.thumbnail(size)
        img.save(outfile)

    return outfile
