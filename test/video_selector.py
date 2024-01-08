from tkinter import filedialog
from PIL import ImageTk, Image
import decord

size = (800, 450)


def select_video():
    video_path = filedialog.askopenfilename()
    video = decord.VideoReader(video_path)
    global img1_file
    frame = video[0]
    img1 = Image.fromarray(frame.asnumpy())
    img1.thumbnail(size)
    img1.show()


if __name__ == '__main__':
    select_video()
