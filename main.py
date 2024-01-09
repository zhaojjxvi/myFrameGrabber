import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import decord
import os


def video_prepare(video_path):
    video_file = decord.VideoReader(video_path)
    video_frame_count = len(video_file)
    video_folder, video_filename = os.path.split(video_path)
    video_f0 = Image.fromarray(video_file[0].asnumpy())
    thumbnail_size = (800, 450)
    video_f0.thumbnail(thumbnail_size)
    video_f0 = ImageTk.PhotoImage(image=video_f0)
    video_details = [video_path, video_frame_count, video_filename, video_folder, video_f0, video_file]
    return video_details


root = tk.Tk()
root.title('FrameParser')
root.geometry('1000x750')

top = tk.Frame(root)
top.pack(side=tk.TOP)

bottom = tk.Frame(root)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# initialization
init_path = 'media/init_video.avi'
video_details = video_prepare(init_path)
video_f0 = video_details[4]

# to place the video frame 0 picture
canvas = tk.Canvas(top, height=500, width=1000)
image_widget = canvas.create_image(500, 25, anchor='n', image=video_f0)
canvas.pack()

# to place a blank space between picture and below widgets
blank_label1_widget = tk.Label(bottom, fg='white', width=20, text='')
blank_label1_widget.pack()


# get video file and display relevant thumbnail picture
def select_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", ".mp4 .avi .mov .wmv"),
                                                       ("All files", "*.*")])

    global video_details
    if video_path == '':
        video_path = video_details[0]  # if not select any video, then use last video file.
    video_details = video_prepare(video_path)
    global video_file
    video_file = video_details[5]
    scale_slider.configure(from_=0, to=len(video_file) - 1, tickinterval=len(video_file) / 10)
    scale_slider.set(0)
    # print(video_details)
    global video_f0
    video_f0 = video_details[4]
    canvas.itemconfigure(image_widget, image=video_f0)


select_video_button = tk.Button(bottom, text='Open Video', width=10, command=select_video)
select_video_button.pack()

def save_img():
    v = scale_slider.get()
    frame = video_file[int(v)]

    img1 = Image.fromarray(frame.asnumpy())  # 将帧转换为PIL Image对象
    img1.save(f'{video_details[0]}_{v}.jpg')  # 将PIL Image保存为图片

save_img_button = tk.Button(bottom, text="Save As.", width=10, command=save_img)
save_img_button.pack()

# to place a blank space
blank_label2_widget = tk.Label(bottom, fg='white', width=20, text='')
blank_label2_widget.pack()

label = tk.Label(bottom, bg='green', fg='white', width=20, text='empty')
label.pack()


def grab_frame(v):
    label.config(text=f'{v}/{video_details[1]}')
    frame = video_file[int(v)]
    img1 = frame.asnumpy()
    img1 = Image.fromarray(img1)
    size = (800, 450)
    img1.thumbnail(size)
    global img1_file
    img1_file = ImageTk.PhotoImage(image=img1)
    canvas.itemconfigure(image_widget, image=img1_file)

    # print(v)


# create a slide for frame select
scale_slider = tk.Scale(bottom, label='Slide to choose frame', from_=0, to=0, orient=tk.HORIZONTAL, length=400,
                        showvalue=False,
                        tickinterval=10, resolution=1, command=grab_frame)
scale_slider.set(0)
scale_slider.pack()


def rewind():
    scale_slider.set(scale_slider.get() - 1)


def ff():
    scale_slider.set(scale_slider.get() + 1)




# create the widgets for the bottom part of the GUI,
# and lay them out
b = tk.Button(bottom, text="Rewind", width=10, height=2, command=rewind)
c = tk.Button(bottom, text="F.F.", width=10, height=2, command=ff)
b.pack(in_=bottom, side=tk.LEFT, expand=True)
c.pack(in_=bottom, side=tk.LEFT, expand=True)


root.mainloop()
