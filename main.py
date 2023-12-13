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
fillColor = "white"
shadowColor = "black"

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
            x, y = 10, 10

            if startTime < ts < endTime:
                """
                Code ripped from here: https://mail.python.org/pipermail/image-sig/2009-May/005681.html
                Yeah had to know how to get PIL to give me text with a shadow outline
                I really do not get it all but alas, it works... I hope.
                """
                # thin border
                d.text((x - 3, y), f'{name}', font=font, fill=shadowColor)
                d.text((x + 3, y), f'{name}', font=font, fill=shadowColor)
                d.text((x, y - 3), f'{name}', font=font, fill=shadowColor)
                d.text((x, y + 3), f'{name}', font=font, fill=shadowColor)

                # thicker border
                d.text((x - 3, y - 3), f'{name}', font=font, fill=shadowColor)
                d.text((x + 3, y - 3), f'{name}', font=font, fill=shadowColor)
                d.text((x - 3, y + 3), f'{name}', font=font, fill=shadowColor)
                d.text((x + 3, y + 3), f'{name}', font=font, fill=shadowColor)

                d.text((x, y), f'{name}', font=font, fill=fillColor)

        # I have no fucking idea don't ask me
        overlay.update(img)
        time.sleep(0.05)
