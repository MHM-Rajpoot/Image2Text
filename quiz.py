from PIL import Image

"""
escape_sequences = ['\\', '\'', '\"', '\n', '\t', '\r', '\b', '\f', '\v']
escape_sequences_ascii = [92,39,34,10,9,13,8,12,11]

for ch,no in zip(escape_sequences,escape_sequences_ascii):
    ch = str(ch)
    ascii = ord(ch)
    nchar = chr(ascii)
    print('Ascii ',ascii,'\t',ascii==no)

#exit()
"""

escape_sequences_dict = {
    10 : 'n',
    9 : 't',
    13 : 'r',
    8: 'b',
    12: 'f',
    11: 'v'
}

def convert_single_backslash(inp:str):
    
    converted_string = ''
    keys = list(escape_sequences_dict.keys())

    for ch in inp:
        
        ascii = ord(ch)
        
        if(ascii in keys):
            newchar = chr(92)  # This 92 will Add BackSlash Once
            newchar += escape_sequences_dict[int(ascii)]
            converted_string += newchar
        else:
            converted_string += ch
    
    return converted_string

def convert_to_jpg(image_path, output_path):
    
    print('After Preprocesssing :: ',image_path)

    try:
        image = Image.open(image_path)
        image = image.convert("RGB")  # Convert image to RGB mode
        image.save(output_path, "JPEG")  # Save as JPEG format
        print("Image converted and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
input_file = 'E:\flet\Image2Text\input\np.PNG'  # Replace with the path to your input image file
output_file = 'output.jpg'  # Replace with the desired path and name for the output image file

input_file = convert_single_backslash(input_file)

convert_to_jpg(input_file, output_file)
