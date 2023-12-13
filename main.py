import time
from PIL import Image, ImageDraw, ImageFont
import mpv
from extractKeys import data

player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)

player.loop_playlist = 'inf'
player.volume = '73'
player.play('files/test-real.mp4')
player.wait_until_playing()

font = ImageFont.truetype('DejaVuSans.ttf', 40)

while not player.core_idle:

    time.sleep(0.5)
    overlay = player.create_image_overlay()
    duration = player.duration
    durtaionToMilliseconds = int(duration*100)

    for pos in range(0, durtaionToMilliseconds, 5):
        # ts is current video time
        ts = player.time_pos
        if ts is None:
            break

        # Colours for the text we will draw, yes colours
        img = Image.new('RGBA', (400, 150),  (255, 255, 255, 0))
        d = ImageDraw.Draw(img)

        # What to show depending on the timestamp e.g. x < ts < y reads as
        # current time greater than 2 but less than 4 do foo
        for x in data:
            name = x['name']
            startTime = x['startTime']
            endTime = x['endTime']

            if startTime < ts < endTime:
                d.text((10, 10), f'{name}', font=font, fill=(0, 255, 255, 128))

        # I have no fucking idea don't ask me
        overlay.update(img)
        time.sleep(0.05)