from chromia.utils import limit


def clip_rgb(rgb):
    rgb._clipped = False
    rgb._unclipped = rgb[0]
    for i in range(4):
        if i < 3:
            if rgb[i] < 0 or rgb[i] > 255:
                rgb._clipped = True
                rgb[i] = limit(rgb[i], 0, 255)
            elif i == 3:
                rgb[i] = limit(rgb[i], 0.0, 1.0)
    return rgb
