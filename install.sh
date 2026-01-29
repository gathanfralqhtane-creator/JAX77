#!/bin/bash

# ===========================================
#   JAX77 - واجهة Termux الفخمة
#   نظام تصميم وتخصيص متكامل
#   المطور: 𝐉𝐀𝐗 ☠️ 𝐏𝐈𝐑𝐀𝐓𝐄-𝐒𝟏
# ===========================================

echo -e "\033[1;31m"
cat << "EOF"

    ██╗ █████╗ ██╗  ██╗███████╗ ██████╗ ██████╗ 
    ██║██╔══██╗╚██╗██╔╝╚══███╔╝██╔═══██╗██╔══██╗
    ██║███████║ ╚███╔╝   ███╔╝ ██║   ██║██████╔╝
██   ██║██╔══██║ ██╔██╗  ███╔╝  ██║   ██║██╔══██╗
╚█████╔╝██║  ██║██╔╝ ██╗███████╗╚██████╔╝██║  ██║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
      𝐓𝐄𝐑𝐌𝐔𝐗 𝐔𝐋𝐓𝐈𝐌𝐀𝐓𝐄 𝐈𝐍𝐓𝐄𝐑𝐅𝐀𝐂𝐄
EOF
echo -e "\033[1;36m"

echo "[*] جاري تثبيت متطلبات JAX77 Hunter..."

# تحديث النظام
pkg update -y && pkg upgrade -y

# تثبيت Python والمكتبات
pkg install -y python python-pip
pkg install -y git figlet

# تثبيت مكتبات Python المطلوبة
pip install colorama pyfiglet

# إنشاء المجلدات اللازمة
mkdir -p ~/.hunter
mkdir -p ~/.hunter/backups

# نسخ الملفات
echo "[*] نسخ ملفات النظام..."
cp hunter.py ~/.hunter/
cp login_system.py ~/.hunter/
cp config.json ~/.hunter/

# منح صلاحيات التنفيذ
chmod +x ~/.hunter/hunter.py
chmod +x ~/.hunter/login_system.py

# نسخ ملف التثبيت إلى النظام
cp install.sh ~/.hunter/

echo "[*] الإعدادات المبدئية..."

# إنشاء ملف تهيئة افتراضي
cat > ~/.hunter/config.json << EOL
{
    "app_name": "HUNTER",
    "figlet_font": "standard",
    "name_color": "red",
    "menu_numbers_color": "cyan",
    "menu_text_color": "white",
    "password": "",
    "login_enabled": false,
    "welcome_message": "مرحباً بك في واجهة JAX77 الفخمة"
}
EOL

echo "[+] تم التثبيت بنجاح!"
echo ""
echo "لبدء الاستخدام، قم بتشغيل:"
echo "python ~/.hunter/hunter.py"
echo ""
echo -e "\033[1;33m[*] إرشادات مهمة:"
echo "- استخدم الخيار 5 لحفظ الواجهة كافتراضية"
echo "- استخدم الخيار 7 لتفعيل نظام الحماية"
echo -e "\033[0m"
