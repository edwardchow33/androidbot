import autopy
import time

print autopy.mouse.location()

autopy.mouse.move(1543,878)
autopy.mouse.toggle(down=True)

autopy.mouse.toggle(down=False)