from spacedetection import CoordinatesGenerator
import yaml

def main():
    image = 'imgs/lot1.png'
    coord_file = 'data/coords.yml'

    #Up to here, the code is collecting coordinates of the parking spaces
    if image is not None:
        with open(coord_file, "w+") as coords:
            gen = CoordinatesGenerator(image, coords, (0, 0, 255))
            gen.generate()

    #Now that we have coordinates, check if the spaces are available. 
    with open(coord_file, "r") as data:
        points = yaml.safe_load(data)
        #Enter protocol for object detection here
    

    print('All Done')

if __name__ == '__main__':
    main()