#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
نظام دخول JAX77 Hunter
"""

import os
import sys
import json
import getpass
from colorama import init, Fore

init(autoreset=True)

CONFIG_FILE = os.path.expanduser("~/.hunter/config.json")

def load_config():
    """تحميل الإعدادات"""
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def show_welcome():
    """عرض رسالة ترحيبية"""
    print(f"\n{Fore.CYAN}{'═'*60}")
    print(f"{Fore.RED}██╗  ██╗ █████╗ ██╗  ██╗███████╗ ██████╗ ██████╗")
    print(f"{Fore.YELLOW}██║  ██║██╔══██╗╚██╗██╔╝╚══███╔╝██╔═══██╗██╔══██╗")
    print(f"{Fore.GREEN}███████║███████║ ╚███╔╝   ███╔╝ ██║   ██║██████╔╝")
    print(f"{Fore.BLUE}██╔══██║██╔══██║ ██╔██╗  ███╔╝  ██║   ██║██╔══██╗")
    print(f"{Fore.MAGENTA}██║  ██║██║  ██║██╔╝ ██╗███████╗╚██████╔╝██║  ██║")
    print(f"{Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝")
    print(f"{Fore.CYAN}{'═'*60}")
    print(f"{Fore.YELLOW}🔒 نظام الدخول الآمن - JAX77 HUNTER")
    print(f"{Fore.CYAN}{'═'*60}\n")

def main():
    """الدالة الرئيسية"""
    config = load_config()
    
    if config.get('login_enabled', False):
        show_welcome()
        
        attempts = 3
        while attempts > 0:
            try:
                password = getpass.getpass(f"{Fore.GREEN}🔑 أدخل كلمة المرور: {Fore.WHITE}")
                
                if password == config.get('password', ''):
                    print(f"\n{Fore.GREEN}✅ تم الدخول بنجاح! مرحباً بك في نظام JAX77...")
                    print(f"{Fore.CYAN}✨ الإصدار: JAX77 Ultimate Edition")
                    return True
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"{Fore.RED}❌ كلمة مرور خاطئة! محاولات متبقية: {attempts}")
                    else:
                        print(f"{Fore.RED}⛔ فشلت جميع المحاولات!")
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}⚠️  تم إلغاء العملية")
                sys.exit(1)
        
        print(f"{Fore.RED}🚫 تم الخروج من النظام...")
        sys.exit(1)
    
    return True

if __name__ == "__main__":
    main()
