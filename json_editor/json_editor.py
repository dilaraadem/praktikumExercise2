import json

def edit_json(filename):

    f = open(filename,'r')
    x = json.load(f)

    # Input required to create a new pedestrian
    id = int(input("Pedestrian ID: "))
    target_id = int(input("Target ID: "))
    x_coordinate = float(input("X coordinate: "))
    y_coordinate = float(input("Y coordinate: "))
    output_filename = input("Please provide the output filename: ")

    #We allow changing Pedestrian ID, Target ID and Pedestrian Location to add the pedestrian to topography.
    pedestrian_json = open('pedestrian_json','r')
    pedestrian_data = json.load(pedestrian_json)
    pedestrian_data['attributes']['id'] = id
    pedestrian_data['position']['x'] = x_coordinate
    pedestrian_data['position']['y'] = y_coordinate
    pedestrian_data['targetIds'] = [target_id]
    append_loc = x['scenario']['topography']['dynamicElements']
    append_loc.append(pedestrian_data)

    #Write the modifications to output file
    writefile = open(output_filename,'w')
    json.dump(x,writefile)

def get_pedestrian_json(filename):

    #This method is used for one time to obtain Pedestrian attributes JSON for future use.
    f = open(filename,'r')
    x = json.load(f)
    str_to_add = x['scenario']['topography']['dynamicElements'][0]
    writefile = open('pedestrian_json','w')
    json.dump(str_to_add,writefile)

def main():
    filename = input("Enter the filename: ")
    edit_json(filename)

if __name__ == '__main__':
    main()