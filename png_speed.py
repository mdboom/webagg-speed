from matplotlib import _png

import time

data = []

for compression in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    for filter in (-1, 'NONE', 'SUB', 'UP', 'AVG', 'PAETH'):
        if not isinstance(filter, int):
            filter_no = getattr(_png, 'PNG_FILTER_' + filter)
        else:
            filter = 'XXX'
            filter_no = -1

        times = 0
        sizes = 0
        for i in range(16):
            filename = 'test{0:04d}.png'.format(i)
            image = _png.read_png_int(filename)

            t = time.time()
            buffer = _png.write_png(image, None, compression=compression, filter=filter_no)
            times += (time.time() - t)
            sizes += len(buffer)

        print(compression, filter, times, sizes)
        data.append((compression, filter, times, sizes))

print(data)
