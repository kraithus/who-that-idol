from PIL import Image
with Image.open("files/members/Asa.jpg") as im:
    im.rotate(45).show()
