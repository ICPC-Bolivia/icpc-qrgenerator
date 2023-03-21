#!/usr/bin/env python
import csv
import os
import qrcode
import sys
from PIL import ImageDraw, ImageFont
from nanoid import generate as nanoid_generate

DIRECTORY_NAME = "./results"
QR_COLOR = (12, 70, 135)
FONT_COLOR = (0, 0, 0)

def generate_qr(file_name, name, team, school, nanoid):
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 20)

    qr = qrcode.QRCode(version=1, box_size=20)
    qr.add_data(nanoid)
    img = qr.make_image(fill_color=QR_COLOR)

    draw = ImageDraw.Draw(img)
    draw.text((140, 30), "ICPC Latin America - 2022", font=font, fill=FONT_COLOR)
    draw.text((80, 505), name, font=font, fill=FONT_COLOR)
    draw.text((80, 525), team, font=font, fill=FONT_COLOR)
    draw.text((80, 548), school, font=font, fill=FONT_COLOR)

    file_name = f"{DIRECTORY_NAME}/{file_name}"
    print(f"Saving image at {file_name}")
    img.save(file_name)


def generate_qrs(file_name, count=1):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            nanoid = row[0]
            name = row[1]
            school = row[2]
            team = row[3]
            generate_qr(f"{str(count).zfill(3)}-{nanoid}.png", name, team, school, nanoid)
            count +=1

def generate_final_csv(csv_file, result_file):
    pass
    with open(result_file, "w") as output:
        with open(csv_file) as input:
            reader = csv.reader(input, delimiter=',')
            for row in reader:
                nanoid = nanoid_generate('1234567890abcdefYXZWQR', 10)
                print(f"{nanoid} ----> {row[0]} / {row[1]} / {row[2]}")
                output.write(f"{nanoid},\"{row[0]}\",{row[1]},{row[2]}\n")

def main():
    if len(sys.argv) < 2:
        print(f'Run as: {sys.argv} <csv_filename>')
        exit(1)

    if not os.path.exists(DIRECTORY_NAME):
        print(f"Creating {DIRECTORY_NAME} directory")
        os.mkdir(DIRECTORY_NAME)

    original_csv = sys.argv[1]
    final_csv = original_csv.replace('.csv', '-final.csv')
    final_csv = f'./results/{final_csv}'
    generate_final_csv(original_csv, final_csv)
    generate_qrs(final_csv, count=1)


if __name__ == "__main__":
    main()
