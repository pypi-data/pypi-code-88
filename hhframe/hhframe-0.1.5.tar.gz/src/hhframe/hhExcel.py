
# -*- codeing = utf-8 -*-
# @File：hhExcel.py
# @Ver：1.0.0
# @Author：立树
# @Time：2021/5/27 16:26
# @IDE：PyCharm

import xlwt

# 设置单元格高度
def setXlsCellHeight(row,height):
    row.height_mismatch = True
    row.height = height * 20                # 20为基准数

# 设置单元格宽度
def setXlsCellsWidth(sheet,widths):
    for i,width in enumerate(widths):
        sheet.col(i).width = width*256      # 256为基准数

# 单元格样式
def getXlsCellStyle(font={},align={}):
    # 字体默认配置
    hhFont = {
        "family": "微软雅黑",
        "size": 10,
    }
    hhAlign = {
        "horz": "left",
        "vert": "center"
    }
    hhAlignHorz = {
        "left": xlwt.Alignment.HORZ_LEFT,
        "center": xlwt.Alignment.HORZ_CENTER,
        "right": xlwt.Alignment.HORZ_RIGHT,
        "filled": xlwt.Alignment.HORZ_FILLED,
        "general": xlwt.Alignment.HORZ_GENERAL,
        "center_across_sel": xlwt.Alignment.HORZ_CENTER_ACROSS_SEL,
        "distributed": xlwt.Alignment.HORZ_DISTRIBUTED,
        "justified": xlwt.Alignment.HORZ_JUSTIFIED
    }
    hhAlignVert = {
        "top": xlwt.Alignment.VERT_TOP,
        "center": xlwt.Alignment.VERT_CENTER,
        "bottom": xlwt.Alignment.VERT_BOTTOM,
        "justified": xlwt.Alignment.VERT_JUSTIFIED,
        "distributed": xlwt.Alignment.VERT_DISTRIBUTED
    }

    hhFont.update(font)
    hhAlign.update(align)

    font = xlwt.Font()
    font.name = hhFont["family"]            # 字体名称
    font.height = hhFont["size"] * 20       # 字体大小，10为字号，20为衡量单位
    # font.colour_index = 4                 # 字体颜色

    align = xlwt.Alignment()
    align.horz = hhAlignHorz[hhAlign["horz"]]
    align.vert = hhAlignVert[hhAlign["vert"]]

    style = xlwt.XFStyle()
    style.font = font
    style.alignment = align

    return style
