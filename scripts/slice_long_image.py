#!/usr/bin/env python3
"""把详情页长截图按高度切成几段，方便逐段看清每一屏。

用法：python3 scripts/slice_long_image.py <长图路径> [输出目录]
每段高度约为宽度的 2 倍，相邻两段重叠 60 像素，文件名里带这一段在原图里的起止位置。
"""
import os
import sys

from PIL import Image


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "./ref-slices"
    os.makedirs(out, exist_ok=True)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    seg, overlap, top, i = w * 2, 60, 0, 1
    while True:
        bottom = min(h, top + seg)
        name = os.path.join(out, f"seg{i:02d}_y{top}-{bottom}.png")
        im.crop((0, top, w, bottom)).save(name)
        print(name)
        if bottom >= h:
            break
        top, i = bottom - overlap, i + 1


if __name__ == "__main__":
    main()
