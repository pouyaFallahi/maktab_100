import argparse, os
parse = argparse.ArgumentParser(description='show total size file or directory')
parse.add_argument('-d','--dir', type=str, required=False, help='After this argument, enter the address of the directory')
parse.add_argument('-f','--file', type=str, required=False, help='After this argument, enter the address of the file')
parse.add_argument('-F','--File', type=str, required=False, help='To calculate all files that are of the same type')
KB = 1024
file = parse.parse_args()

if file.dir and file.File == False:
    if os.path.exists(file.dir):
         print(f'{KB/os.path.getsize(file.dir)} KB')


    else:
        print('file or directory not find!!!!!')


elif file.file:
    if os.path.exists(file.file):
        print(f'{KB/os.path.getsize(file.file)} KB')
    else:
        print('file or directory not find!!!!!')

if file.File and file.dir:
    format = file.File
    total = 0
    count = 0
    if os.path.exists(file.dir):
        for root, dirs, file in os.walk(file.dir):
            for i in file:
                if i.endswith(format):
                    file_path = os.path.join(root, i)
                    total += os.path.getsize(file_path)
                    count += 1
        print(f'{KB / total}KB \nmeny: {count}')


    else:
        print('file or directory not find!!!!!')



else:
    print('Check the entry!!!!')