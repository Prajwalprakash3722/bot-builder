import pyautogui
import pygetwindow
from PIL import Image

print(pygetwindow.getAllTitles())


def get_screen_shot():
    # get the screen shot
    image = pyautogui.screenshot("snake_board_game")
    # convert the image to a png
    image.save("screen.png")
    # convert the image to a numpy array
    image = np.array(image)
    # convert the image to a numpy array
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
