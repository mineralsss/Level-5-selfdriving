import screen_grab
import image_process
feed = "https://www.youtube.com/watch?v=KBsqQez-O4w"
if __name__== "__main__":
    while True:
        feed = screen_grab.get_screenshot()
        image_process.tracking(feed)