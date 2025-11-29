import base64
import marshal
import os
import time
from pystyle import Colors, Colorate
from rich.console import Console

console = Console()

def encode_file_to_exec_code(file_path, output_file):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
        
        bytecode = compile(source_code, file_path, 'exec')
        marshaled_code = marshal.dumps(bytecode)
        encoded_code = base64.a85encode(marshaled_code)
        exec_code = f"exec(__import__('marshal').loads(__import__('base64').a85decode({encoded_code!r})))"
        
        with open(output_file, 'w') as output:
            output.write(exec_code)
        
        print(Colorate.Diagonal(Colors.purple_to_blue, f"Code has been encrypted and saved to file {output_file}"))
    
    except Exception as e:
        print(Colorate.Diagonal(Colors.red_to_black, f"Error during encryption: {e}"))

def custom_print(text, color, interval):
    for char in text:
        console.print(char, style=color, end="")
        time.sleep(interval)
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    custom_print(r"""
                                                                    
                         ,--.                                  ,--. 
   ,---,               ,--.'|            ,---,               ,--.'| 
  '  .' \          ,--,:  : |           '  .' \          ,--,:  : | 
 /  ;    '.     ,`--.'`|  ' :          /  ;    '.     ,`--.'`|  ' : 
:  :       \    |   :  :  | |         :  :       \    |   :  :  | | 
:  |   /\   \   :   |   \ | :         :  |   /\   \   :   |   \ | : 
|  :  ' ;.   :  |   : '  '; |         |  :  ' ;.   :  |   : '  '; | 
|  |  ;/  \   \ '   ' ;.    ;         |  |  ;/  \   \ '   ' ;.    ; 
'  :  | \  \ ,' |   | | \   |         '  :  | \  \ ,' |   | | \   | 
|  |  '  '--'   '   : |  ; .'         |  |  '  '--'   '   : |  ; .' 
|  :  :         |   | '`--'           |  :  :         |   | '`--'   
|  | ,'         '   : |               |  | ,'         '   : |       
`--''           ;   |.'               `--''           ;   |.'       
                '---'                                 '---'         
    ╔══════════════════════════════════════════════════════╗
    ║     𝐃𝐀𝐓𝐀 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐎𝐍 𝐕2  | 𝐃𝐄𝐕𝐄𝐋𝐎𝐏 𝐁𝐘: 𝐀𝐍             ║
    ╚══════════════════════════════════════════════════════╝                      
""", "purple", 0.0009)
    
    time.sleep(1)
    
    input_dir = 'FilesToEncrypt'
    output_dir = 'EncryptedFiles'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_name = input(Colorate.Diagonal(Colors.purple_to_blue, "Enter the file to be encrypted: "))
    
    file_path = os.path.join(input_dir, file_name)
    if os.path.isfile(file_path):
        output_file = os.path.join(output_dir, f"enc_{file_name}")
        encode_file_to_exec_code(file_path, output_file)
    else:
        print(Colorate.Diagonal(Colors.purple_to_blue, f"File '{file_name}' does not exist in the directory '{input_dir}'."))

if __name__ == '__main__':
    main()