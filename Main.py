import base64
import marshal
import os
import requests
import concurrent.futures
import time
from pystyle import Colors, Colorate

from rich.console import Console
import time
from time import sleep

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

        print(Colorate.Diagonal(Colors.purple_to_blue,f"Mã đã mã hóa và lưu vào file {output_file} thành công."))

    except Exception as e:
        print(Colorate.Diagonal(Colors.red_to_black,f"Lỗi khi mã hóa: {e}"))
from rich.console import Console
import time

console = Console()

def custom_print(text, color, interval):
    for char in text:
        console.print(char, style=color, end="")
        time.sleep(interval)
    print()  

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    custom_print("""
                                                                    
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
    ║     𝐃𝐀𝐓𝐀 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐎𝐍 𝐕2  | 𝐃𝐄𝐕𝐄𝐋𝐎𝐏 𝐁𝐘: 𝐀𝐍 𝐀𝐍          ║
    ╚══════════════════════════════════════════════════════╝                      
\n""","purple", 0.0009)
    sleep(1)
  
  
    # Thư mục chứa file cần mã hóa và thư mục lưu file mã hóa
    # Thư mục chứa file cần mã hóa và thư mục lưu file mã hóa
    input_dir = 'FileCanMaHoa'
    output_dir = 'FileDaMaHoa'

    # Kiểm tra xem thư mục đích có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

  
    file_name = input(Colorate.Diagonal(Colors.purple_to_blue,f"nhập file cần mã hóa : "))

  
    file_path = os.path.join(input_dir, file_name)
    if os.path.isfile(file_path):
        output_file = os.path.join(output_dir, f"enc_{file_name}")  
        encode_file_to_exec_code(file_path, output_file)
    else:
        print(Colorate.Diagonal(Colors.purple_to_blue,f"File '{file_name}' không tồn tại trong thư mục '{input_dir}'."))

if __name__ == '__main__':

    
    main()  # Gọi hàm main
