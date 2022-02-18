import tempfile
import os

import pyautogui
import img2pdf

# Mostly stolen from vitalsource-printer here: https://github.com/manhtai/vitalsource-printer
# adapted to use pyautogui instead of autopy
def screenshot(top_left, bottom_right, next_page_loc, total_page_num):
    pic_size = (bottom_right[0] - top_left[0], bottom_right[1] - top_left[1])
    combined_tuple = (top_left[0], top_left[1], pic_size[0], pic_size[1])
    images = []
    temp_dir = tempfile.mkdtemp()
    for i in range(total_page_num):
        page_num = "{}".format(i).zfill(len(str(total_page_num)))
        file_name = os.path.join(temp_dir, 'book-page-{}.png'.format(page_num))
        images.append(file_name)

        pyautogui.moveTo(next_page_loc)
        pyautogui.click(interval=1.0) # 1s pause between actions to be sure the page loads. This can be lowered, but be careful, its taking control of your mouse
        pyautogui.screenshot(region=combined_tuple).save(file_name) # left, top, width, height

    return images

def convert(images):
    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert(images))


if __name__ == "__main__":
    tl, br, nxt, ttl = "", "", "", ""

    with open("coordinfo.txt", "r") as f:
        tl = f.readline()
        br = f.readline()
        nxt = f.readline()
        ttl = f.readline()

    top_left = tuple(map(lambda x: int(x), tl.split(',')))
    bottom_right = tuple(map(lambda x: int(x), br.split(',')))
    next_button_loc = tuple(map(lambda x: int(x), nxt.split(',')))
    total_pages = int(ttl)

    print("Taking screenshots using inputs: {} {} {} {}".format(top_left, bottom_right, next_button_loc, total_pages))

    images = screenshot(top_left, bottom_right, next_button_loc, total_pages)
    convert(images)
    print("Done, book saved as book.pdf")
