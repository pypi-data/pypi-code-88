import io
from typing import List

import fitz
from fitz import Pixmap

__all__ = [
    'pdf_to_png',
]


def pdf_to_png(data: bytes, limit=None) -> List[bytes]:
    result = []
    pdf = fitz.Document(stream=io.BytesIO(data), filetype='pdf')
    for i, page in enumerate(pdf):
        # 将每一页pdf读取为图片
        img: Pixmap = page.getPixmap()
        result.append(img.tobytes())

        if limit is not None and len(result) >= limit:
            break
    return result
