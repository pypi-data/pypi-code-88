import time
import cartils.enums as enums
import encoding
import multiprocessing

class Animation:
    def __init__(self):
        self.ANIMATION = []
        self.MAX_LINE_WIDTH = 48
        self.animation_process = None
        self.formatting = {
            '[BLACK]': enums.Colors.BLACK.value,
            '[RED]': enums.Colors.RED.value,
            '[GREEN]': enums.Colors.GREEN.value,
            '[YELLOW]': enums.Colors.YELLOW.value,
            '[BLUE]': enums.Colors.BLUE.value,
            '[MAGENTA]': enums.Colors.MAGENTA.value,
            '[CYAN]': enums.Colors.CYAN.value,
            '[WHITE]': enums.Colors.WHITE.value,
            '[RESET]': enums.Colors.RESET.value,
            '[BOLD]': enums.Colors.BOLD.value,
            '[UNDERLINE]': enums.Colors.UNDERLINE.value,
            '[REVERSED]': enums.Colors.REVERSED.value
        }

    def run(self, frame_count=-1, refresh_rate=0.25, loop=False):
        i = 0
        counter = 0
        while counter < frame_count:
            for j in range(0, len(self.ANIMATION[0])):
                line = self.ANIMATION[i % len(self.ANIMATION)][j]
                for k in self.formatting:
                    line = line.replace(k, self.formatting[k])
                print(line)
            time.sleep(refresh_rate)
            for j in range(0, len(self.ANIMATION[0])):
                print ("\033[A{}\033[A".format(' ' * self.MAX_LINE_WIDTH))
            i += 1
            i = i % len(self.ANIMATION)
            if loop:
                if counter == frame_count - 1:
                    counter = -1
                    i = 0
            counter += 1
            
    def run_async(self, frame_count=-1, refresh_rate=0.25, loop=False):
        self.animation_process = None
        self.animation_process = multiprocessing.Process(target=self.run, args=(frame_count, refresh_rate, loop))
        self.animation_process.start()
                
    def stop_async(self):
        if self.animation_process:
            self.animation_process.terminate()

    def read_animation(self, f_name, line_count, skip_line=True, rle=False):
        with open(f_name) as f:
            if rle:
                lines = encoding.RLE.decode(f).split('\n')
            else:
                lines = f.read().split('\n')
        index = 0
        data = []
        while index < len(lines):
            frame = []
            for i in range(0, line_count):
                frame.append(lines[index])
                index += 1
            data.append(frame)
            if skip_line:
                index += 1
        self.ANIMATION = data

if __name__ == '__main__':
    ff = Animation()
    ff.read_animation('credits.txt', 14)
    ff.run(frame_count=24)
    print('Now add a little bit of _spice_')
    ff.read_animation('credits.rle', 14, rle=True)
    ff.run(frame_count=24)
    print('now for some async')
    ff.run_async(frame_count=24)
    time.sleep(1)
    ff.stop_async()