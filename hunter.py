#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JAX77 HUNTER - واجهة Termux الفخمة
تم التطوير بواسطة: 𝐉𝐀𝐗 ☠️ 𝐏𝐈𝐑𝐀𝐓𝐄-𝐒𝟏
"قائد لواء العدناني - نحن لا نصنع الأدوات، نحن نصنع التاريخ"
"""

import os
import sys
import json
import subprocess
import time
from colorama import init, Fore, Style, Back
from pyfiglet import Figlet

# تهيئة Colorama للتعامل مع الألوان
init(autoreset=True)

# مسار ملف الإعدادات
CONFIG_FILE = os.path.expanduser("~/.hunter/config.json")

class HunterInterface:
    """الفئة الرئيسية لواجهة HUNTER"""
    
    def __init__(self):
        """تهيئة الواجهة وتحميل الإعدادات"""
        self.load_config()
        self.colors_map = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE
        }
        self.fonts_list = ['standard', 'slant', 'shadow', 'small', 'block', 'bubble', 'digital']
        
    def load_config(self):
        """تحميل الإعدادات من ملف JSON"""
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except:
            # إعدادات افتراضية
            self.config = {
                "app_name": "HUNTER",
                "figlet_font": "standard",
                "name_color": "red",
                "menu_numbers_color": "cyan",
                "menu_text_color": "white",
                "password": "",
                "login_enabled": False,
                "welcome_message": "مرحباً بك في واجهة JAX77 الفخمة"
            }
            self.save_config()
    
    def save_config(self):
        """حفظ الإعدادات إلى ملف JSON"""
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
    
    def clear_screen(self):
        """مسح الشاشة"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_banner(self):
        """عرض البانر الرئيسي بخط FIGlet"""
        self.clear_screen()
        
        # إنشاء كائن Figlet مع الخط المحدد
        figlet = Figlet(font=self.config['figlet_font'])
        
        # الحصول على لون الاسم من الخريطة
        name_color = self.colors_map.get(self.config['name_color'], Fore.RED)
        
        # عرض الاسم بألوان متدرجة
        banner_text = figlet.renderText(self.config['app_name'])
        lines = banner_text.split('\n')
        
        print("\n" + "="*60)
        for i, line in enumerate(lines):
            if line.strip():
                # تدرج لوني فريد
                if i % 3 == 0:
                    print(name_color + line)
                elif i % 3 == 1:
                    print(Fore.YELLOW + line)
                else:
                    print(Fore.CYAN + line)
        
        print("="*60)
        print(f"\n{Fore.GREEN}🎯 {self.config['welcome_message']}")
        print(f"{Fore.MAGENTA}⚡ النسخة: JAX77 Ultimate Edition")
        print(f"{Fore.CYAN}✨ المطور: 𝐉𝐀𝐗 ☠️ 𝐏𝐈𝐑𝐀𝐓𝐄-𝐒𝟏\n")
    
    def print_menu(self):
        """عرض القائمة الرئيسية مع تخصيص الألوان"""
        menu_items = [
            "[1] تغيير اسم الواجهة",
            "[2] تغيير ستايل الخط",
            "[3] تغيير لون الاسم",
            "[4] تغيير لون نصوص القائمة",
            "[5] حفظ الواجهة كافتراضية",
            "[6] معلومات المطور",
            "[7] قفل الأمان (نظام دخول)",
            "[8] خروج من الأداة"
        ]
        
        numbers_color = self.colors_map.get(self.config['menu_numbers_color'], Fore.CYAN)
        text_color = self.colors_map.get(self.config['menu_text_color'], Fore.WHITE)
        
        print(f"{numbers_color}{Style.BRIGHT}📜 القائمة الرئيسية:\n")
        for item in menu_items:
            # فصل الرقم عن النص
            parts = item.split(']', 1)
            if len(parts) == 2:
                print(f"{numbers_color}{parts[0]}]{text_color}{parts[1]}")
        
        print(f"\n{Fore.YELLOW}{'═'*60}")
    
    def change_app_name(self):
        """تغيير اسم الواجهة"""
        print(f"\n{Fore.CYAN}✨ الإسم الحالي: {self.config['app_name']}")
        new_name = input(f"{Fore.GREEN}🎯 أدخل الاسم الجديد: {Fore.YELLOW}")
        
        if new_name.strip():
            self.config['app_name'] = new_name.strip()
            self.save_config()
            print(f"{Fore.GREEN}✅ تم تغيير الاسم بنجاح!")
        else:
            print(f"{Fore.RED}❌ الاسم لا يمكن أن يكون فارغاً!")
        
        input(f"\n{Fore.CYAN}🎯 اضغط Enter للمتابعة...")
    
    def change_font_style(self):
        """تغيير ستايل الخط"""
        print(f"\n{Fore.CYAN}✨ الخط الحالي: {self.config['figlet_font']}")
        print(f"{Fore.GREEN}📝 اختر نوع الخط من القائمة:")
        
        for i, font in enumerate(self.fonts_list, 1):
            print(f"{Fore.YELLOW}[{i}] {font}")
        
        try:
            choice = int(input(f"\n{Fore.GREEN}🎯 أدخل رقم الخط المطلوب (1-7): {Fore.YELLOW}"))
            if 1 <= choice <= 7:
                self.config['figlet_font'] = self.fonts_list[choice-1]
                self.save_config()
                print(f"{Fore.GREEN}✅ تم تغيير الخط بنجاح!")
            else:
                print(f"{Fore.RED}❌ الرقم خارج النطاق!")
        except:
            print(f"{Fore.RED}❌ إدخال غير صالح!")
        
        input(f"\n{Fore.CYAN}🎯 اضغط Enter للمتابعة...")
    
    def change_name_color(self):
        """تغيير لون الاسم"""
        colors = list(self.colors_map.keys())
        print(f"\n{Fore.CYAN}✨ اللون الحالي: {self.config['name_color']}")
        print(f"{Fore.GREEN}🎨 اختر لوناً جديداً:")
        
        for i, color in enumerate(colors, 1):
            color_code = self.colors_map[color]
            print(f"{color_code}[{i}] {color}")
        
        try:
            choice = int(input(f"\n{Fore.GREEN}🎯 أدخل رقم اللون المطلوب (1-7): {Fore.YELLOW}"))
            if 1 <= choice <= 7:
                self.config['name_color'] = colors[choice-1]
                self.save_config()
                print(f"{Fore.GREEN}✅ تم تغيير اللون بنجاح!")
            else:
                print(f"{Fore.Red}❌ الرقم خارج النطاق!")
        except:
            print(f"{Fore.RED}❌ إدخال غير صالح!")
          input(f"\n{Fore.CYAN}🎯 اضغط Enter للمتابعة...")
    
    def change_menu_colors(self):
        """تغيير ألوان القائمة"""
        colors = list(self.colors_map.keys())
        
        print(f"\n{Fore.CYAN}✨ ألوان القائمة الحالية:")
        print(f"   أرقام القائمة: {self.config['menu_numbers_color']}")
        print(f"   نصوص القائمة: {self.config['menu_text_color']}")
        
        print(f"\n{Fore.GREEN}🎨 اختر لوناً للأرقام:")
        for i, color in enumerate(colors, 1):
            color_code = self.colors_map[color]
            print(f"{color_code}[{i}] {color}")
        
        try:
            choice = int(input(f"\n{Fore.GREEN}🎯 أدخل رقم اللون للأرقام (1-7): {Fore.YELLOW}"))
            if 1 <= choice <= 7:
                self.config['menu_numbers_color'] = colors[choice-1]
                
                print(f"\n{Fore.GREEN}🎨 اختر لوناً للنصوص:")
                for i, color in enumerate(colors, 1):
                    color_code = self.colors_map[color]
                    print(f"{color_code}[{i}] {color}")
                
                choice2 = int(input(f"\n{Fore.GREEN}🎯 أدخل رقم اللون للنصوص (1-7): {Fore.YELLOW}"))
                if 1 <= choice2 <= 7:
                    self.config['menu_text_color'] = colors[choice2-1]
                    self.save_config()
                    print(f"{Fore.GREEN}✅ تم تغيير ألوان القائمة بنجاح!")
                else:
                    print(f"{Fore.RED}❌ الرقم خارج النطاق!")
            else:
                print(f"{Fore.RED}❌ الرقم خارج النطاق!")
        except:
            print(f"{Fore.RED}❌ إدخال غير صالح!")
        
        input(f"\n{Fore.CYAN}🎯 اضغط Enter للمتابعة...")
    
    def save_as_default(self):
        """حفظ الواجهة كافتراضية في Termux"""
        print(f"\n{Fore.YELLOW}⚠️  تحذير: هذا الإجراء سيضيف الأداة لبدء التشغيل التلقائي")
        confirm = input(f"{Fore.GREEN}🎯 هل أنت متأكد؟ (نعم/لا): {Fore.YELLOW}").lower()
        
        if confirm in ['نعم', 'yes', 'y', 'ye']:
            try:
                bashrc_path = os.path.expanduser("~/.bashrc")
                hunter_path = os.path.expanduser("~/.hunter/hunter.py")
                
                # إضافة أمر التشغيل إلى .bashrc
                with open(bashrc_path, 'a', encoding='utf-8') as f:
                    f.write(f'\n# JAX77 Hunter Interface - Auto Start\n')
                    f.write(f'python {hunter_path}\n')
                
                print(f"{Fore.GREEN}✅ تم إضافة الأداة للبدء التلقائي!")
                print(f"{Fore.CYAN}📁 المسار: {bashrc_path}")
            except Exception as e:
                print(f"{Fore.RED}❌ حدث خطأ: {e}")
        else:
            print(f"{Fore.YELLOW}❌ تم إلغاء العملية")
        
        input(f"\n{Fore.CYAN}🎯 اضغط Enter للمتابعة...")
    
    def show_developer_info(self):
        """عرض معلومات المطور بواجهة فخمة"""
        self.clear_screen()
        
        print(f"\n{Fore.CYAN}{'═'*60}")
        print(f"{Fore.RED}{'★'*25} معلومات المطور {'★'*25}")
        print(f"{Fore.CYAN}{'═'*60}\n")
        
        # عرض معلومات المطور بتصميم فني
        dev_info = [
            f"{Fore.YELLOW}╔══════════════════════════════════════════════════╗",
            f"{Fore.YELLOW}║ {Fore.CYAN}👑 المطور: {Fore.GREEN}𝐉𝐀𝐗 ☠️ 𝐏𝐈𝐑𝐀𝐓𝐄-𝐒𝟏",
            f"{Fore.YELLOW}║ {Fore.CYAN}🏴 القائد: {Fore.MAGENTA}قائد لواء العدناني",
            f"{Fore.YELLOW}║ {Fore.CYAN}🎯 العبارة: {Fore.WHITE}نحن لا نصنع الأدوات، نحن نصنع التاريخ",
            f"{Fore.YELLOW}║ ",
            f"{Fore.YELLOW}║ {Fore.CYAN}📅 سنة التأسيس: {Fore.GREEN}2024",
            f"{Fore.YELLOW}║ {Fore.CYAN}⚡ الإصدار: {Fore.MAGENTA}JAX77 Ultimate",
            f"{Fore.YELLOW}║ {Fore.CYAN}🎨 التصميم: {Fore.BLUE}واجهة فريدة ثلاثية الأبعاد",
            f"{Fore.YELLOW}║ ",
            f"{Fore.YELLOW}║ {Fore.RED}⚠️  تحذير:",
            f"{Fore.YELLOW}║ {Fore.WHITE}هذه الأداة للاستخدام الأخلاقي فقط",
            f"{Fore.YELLOW}║ {Fore.WHITE}جميع الحقوق محفوظة لفريق العدناني",
            f"{Fore.YELLOW}╚══════════════════════════════════════════════════╝"
        ]
        
        for line in dev_info:
            print(line)
        
        print(f"\n{Fore.CYAN}{'═'*60}")
        input(f"\n{Fore.GREEN}🎯 اضغط Enter للعودة للقائمة الرئيسية...")
    
    def security_lock(self):
        """تفعيل/تعطيل نظام قفل الأمان"""
        print(f"\n{Fore.YELLOW}🔒 نظام حماية واجهة HUNTER\n")
        
        if self.config['login_enabled']:
            print(f"{Fore.CYAN}✨ النظام مفعل حالياً")
            choice = input(f"{Fore.GREEN}🎯 هل تريد تعطيله؟ (نعم/لا): {Fore.YELLOW}").lower()
            
            if choice in ['نعم', 'yes', 'y']:
                self.config['login_enabled'] = False
                self.save_config()
                print(f"{Fore.GREEN}✅ تم تعطيل نظام الحماية!")
        else:
            print(f"{Fore.CYAN}✨ النظام معطل حالياً")
            choice = input(f"{Fore.GREEN}🎯 هل تريد تفعيله؟ (نعم/لا): {Fore.YELLOW}").lower()
            
            if choice in ['نعم', 'yes', 'y']:
                password = input(f"{Fore.GREEN}🔑 أدخل كلمة المرور الجديدة: {Fore.YELLOW}")
                confirm = input(f"{Fore.GREEN}🔑 أعد إدخال كلمة المرور: {Fore.YELLOW}")
                
                if password == confirm:
                    self.config['password'] = password
                    self.config['login_enabled'] = True
                    self.save_config()
                    
                    # إنشاء ملف نظام الدخول
                    login_script = os.path.expanduser("~/.hunter/login_system.py")
                    self.create_login_system(login_script)
                    
                    # إضافة للنظام
                    bashrc_path = os.path.expanduser("~/.bashrc")
                    with open(bashrc_path, 'a', encoding='utf-8') as f:
                        f.write(f'\n# JAX77 Login System\n')
                        f.write(f'python {login_script}\n')
                    
                    print(f"{Fore.GREEN}✅ تم تفعيل نظام الحماية بنجاح!")
                    print(f"{Fore.CYAN}🔐 سيُطلب كلمة المرور عند فتح Termux")
                else:
                    print(f"{Fore.RED}❌ كلمات المرور غير متطابقة!")
        
        input(f"\n{Fore.CYAN}🎯 اضغط Enter للمتابعة...")
    
    def create_login_system(self, filepath):
        """إنشاء نظام الدخول"""
        login_code = '''#!/usr/bin/env python3
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

def main():
    """الدالة الرئيسية"""
    config = load_config()
    
    if config.get('login_enabled', False):
        print(f"\\n{Fore.CYAN}╔{'═'*50}╗")
        print(f"{Fore.CYAN}║{Fore.YELLOW}{'🔒 JAX77 HUNTER - نظام الدخول الآمن'.center(50)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}╚{'═'*50}╝\\n")
        
        attempts = 3
        while attempts > 0:
            try:
                password = getpass.getpass(f"{Fore.GREEN}🔑 أدخل كلمة المرور: ")
                
                if password == config.get('password', ''):
                    print(f"{Fore.GREEN}✅ تم الدخول بنجاح! مرحباً بك...")
                    return True
                else:
                    attempts -= 1
                    print(f"{Fore.RED}❌ كلمة مرور خاطئة! محاولات متبقية: {attempts}")
            except KeyboardInterrupt:
                print(f"\\n{Fore.YELLOW}⚠️  تم إلغاء العملية")
                sys.exit(1)
        
        print(f"{Fore.RED}⛔ فشلت جميع المحاولات! الخروج...")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(login_code)
        
        # منح صلاحيات التنفيذ
        os.chmod(filepath, 0o755)
    
    def run(self):
        """تشغيل الواجهة الرئيسية"""
        while True:
            self.print_banner()
            self.print_menu()
            
            try:
                choice = input(f"\n{Fore.GREEN}🎯 اختر رقم الأمر (1-8): {Fore.YELLOW}")
                
                if choice == '1':
                    self.change_app_name()
                elif choice == '2':
                    self.change_font_style()
                elif choice == '3':
                    self.change_name_color()
                elif choice == '4':
                    self.change_menu_colors()
                elif choice == '5':
                    self.save_as_default()
                elif choice == '6':
                    self.show_developer_info()
                elif choice == '7':
                    self.security_lock()
                elif choice == '8':
                    print(f"\n{Fore.CYAN}👋 مع السلامة... إلى اللقاء!")
                    print(f"{Fore.YELLOW}✨ شكراً لاستخدامك JAX77 Hunter!")
                    time.sleep(2)
                    self.clear_screen()
                    break
                else:
                    print(f"{Fore.RED}❌ رقم غير صالح! اختر من 1 إلى 8")
                    time.sleep(1.5)
            
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}⚠️  تم إلغاء العملية")
                time.sleep(1)
                break
            except Exception as e:
                print(f"{Fore.RED}❌ حدث خطأ: {e}")
                time.sleep(2)

def main():
    """الدالة الرئيسية لتشغيل البرنامج"""
    try:
        # التحقق من وجود المتطلبات
        try:
            import colorama
            import pyfiglet
        except ImportError:
            print(f"{Fore.RED}❌ المكتبات المطلوبة غير مثبتة!")
            print(f"{Fore.YELLOW}✨ قم بتشغيل: pip install colorama pyfiglet")
            return
        
        # تشغيل الواجهة
        app = HunterInterface()
        app.run()
    
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 مع السلامة!")
    except Exception as e:
        print(f"{Fore.RED}❌ خطأ غير متوقع: {e}")

if __name__ == "__main__":
    main()
