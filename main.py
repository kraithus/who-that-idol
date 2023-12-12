import time
from PIL import Image, ImageDraw, ImageFont
import mpv

player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)

player.loop_playlist = 'inf'
player.volume = '73'
player.play('files/test-gidle.mp4')
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
        if 2 < ts < 4:
            d.text((10, 10), 'ITZY', font=font, fill=(0, 255, 255, 128))
            d.text((10, 60), f'{duration:.3f}', font=font, fill=(0, 255, 255, 128))
        if 5 < ts < 9:
            d.text((10, 10), 'Kweenka', font=font, fill=(0, 255, 255, 128))
            d.text((10, 60), f'{duration:.3f}', font=font, fill=(0, 255, 255, 128))
        if 10 < ts < 15:
            d.text((10, 10), 'Test-San', font=font, fill=(0, 255, 255, 128))
            d.text((10, 60), f'{duration:.3f}', font=font, fill=(0, 255, 255, 128))
        if 17 < ts < 23:
            d.text((10, 10), 'Baka-Sama', font=font, fill=(0, 255, 255, 128))
            d.text((10, 60), f'{duration:.3f}', font=font, fill=(0, 255, 255, 128))
        if 178 < ts < 180:
            d.text((10, 10), 'Baka-Sama', font=font, fill=(0, 255, 255, 128))
            d.text((10, 60), f'{duration:.3f}', font=font, fill=(0, 255, 255, 128))
            
        # I have no fucking idea don't ask me
        overlay.update(img)
        time.sleep(0.05)

