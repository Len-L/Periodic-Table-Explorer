import periodictable
from colorama import Fore, Style
import sys

def show_credits():
    print(f"\n{Fore.YELLOW}=== CREDITS ===")
    print(f"{Fore.CYAN}Periodic Table Explorer v1.1")
    print(f"Dikembangkan oleh: {Fore.GREEN}LeonTech{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Youtube: {Fore.GREEN}https://youtube.com/@LenL_")
    print(f"{Fore.CYAN}Terakhir update: {Fore.GREEN}20-04-2025")
    print(f"{Fore.BLUE}Fitur Utama:")
    print("- Pencarian elemen by nama/simbol/nomor")
    print("- Tampilan berwarna interaktif")
    print(f"{Style.RESET_ALL}")

def get_element_info(input_str):
    try:
        if input_str.isdigit():
            return periodictable.elements[int(input_str)]
        elif len(input_str) <= 3:
            for el in periodictable.elements:
                if el.symbol.lower() == input_str.lower():
                    return el
        else:
            for el in periodictable.elements:
                if el.name.lower() == input_str.lower():
                    return el
        return None
    except (AttributeError, ValueError):
        return None

def display_element_info(element):
    print(f"\n{Fore.GREEN}=== {element.name} ({element.symbol}) ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}Nomor Atom:{Style.RESET_ALL} {element.number}")
    print(f"{Fore.CYAN}Massa Atom:{Style.RESET_ALL} {element.mass:.4f} g/mol")
    
    density = element.density if hasattr(element, 'density') else 'N/A'
    print(f"{Fore.CYAN}Densitas:{Style.RESET_ALL} {density} g/cm³")
    
    if hasattr(element, 'description'):
        print(f"{Fore.BLUE}Deskripsi:{Style.RESET_ALL} {element.description}")

def interactive_mode():
    show_credits()
    print(f"{Fore.YELLOW}\nPeriodic Table Explorer")
    print("========================")
    print("Perintah: nama/simbol/nomor | list | exit")
    
    while True:
        user_input = input("\nMasukkan elemen/perintah> ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Terima kasih! Sampai jumpa!")
            sys.exit()
            
        if user_input.lower() == 'list':
            print("\nDaftar Elemen:")
            for el in periodictable.elements:
                if el.number > 0:
                    print(f"{el.number:3} {el.symbol:3} {el.name}")
            continue
            
        element = get_element_info(user_input)
        
        if element and element.number > 0:
            display_element_info(element)
        else:
            print(f"{Fore.RED}Error: Elemen '{user_input}' tidak ditemukan!{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        interactive_mode()
    except KeyboardInterrupt:
        print("\nProgram dihentikan")
        sys.exit(0)





