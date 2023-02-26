from spacedetection import CoordinatesGenerator

def main():
    image = 'imgs/lot1.png'
    coord_file = 'data/coords.yml'

    if image is not None:
        with open(coord_file, "w+") as coords:
            gen = CoordinatesGenerator(image, coords, (0, 0, 255))
            gen.generate()

    print('All Done')

if __name__ == '__main__':
    main()