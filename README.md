نام: شیلان خدری

شماره دانشجویی: 40117023126

صفحه گیتهاب: https://github.com/ShilanKhedri


نحوه اجرا
اجرای سرور:

python server.py

سرور روی 127.0.0.1:12345 اجرا می‌شود.

اجرای کلاینت:

python client.py

برای فازهای 1-3: پیام‌ها از طریق ترمینال ارسال/دریافت می‌شوند.

برای فاز 4: رابط کاربری گرافیکی باز می‌شود.

دستورات:

/exit: خروج از چت.

/pm <userIP> <message>: ارسال پیام خصوصی (فاز 4).

/list: نمایش کاربران متصل (فاز 4).

ساختار پروژه


server.py: کد سرور برای مدیریت اتصال‌ها و پیام‌ها.

client.py: کد کلاینت برای اتصال به سرور و چت.



معماری تمیز با نام‌گذاری مناسب و مدیریت خطاها.

فازهای پروژه

فاز اول: ارتباط اولیه
سرور پیام «سلام سرور!» را دریافت و پاسخ «سلام کلاینت!» را ارسال می‌کند.
اتصال به‌درستی بسته می‌شود.

فاز دوم: چندین کلاینت
سرور با Threading چندین کلاینت را مدیریت می‌کند.
پیام‌های اتصال/قطع اتصال با IP کلاینت ثبت می‌شوند.

فاز سوم: پیام‌های گروهی
پیام یک کلاینت به همه ارسال می‌شود.
پیام‌ها با IP فرستنده نمایش داده می‌شوند.
دستور /exit برای خروج.

فاز چهارم: رابط کاربری
رابط گرافیکی با tkinter.
پیام خصوصی با /pm.
نمایش نام کاربری، زمان، و لیست کاربران با /list.
مدیریت خطاها.
