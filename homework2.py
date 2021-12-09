class SizeException(Exception):
    pass

def func (user_file, num_of_symbols):
    with open(f"{user_file}", 'r') as f:
        file = f.read()

    if len(file) > num_of_symbols:
        center_text = (len(file)+1) // 2
        center = file[int(center_text-num_of_symbols/2):int(center_text+num_of_symbols/2)]
        print(f'Start:{file[:num_of_symbols]}')
        print(f'Middle: {center}')
        print(f'End: {file[-num_of_symbols:]}')
    else:   
        raise SizeException ("Invalid size of file")

        
func('qwerty.txt',int(input("Enter number: ")))