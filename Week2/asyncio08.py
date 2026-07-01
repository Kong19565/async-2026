# โปรแกรม 8: การสลับการทำงานสลับไปมา (Context Switching)
# คอนเซปต์: การเฝ้าดูการสลับงานไปมาของเธรดเดี่ยวระหว่างงานที่แตกต่างกันสองงานโดยใช้ create_task
import asyncio
from time import ctime

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodle in boiling water...")
    await asyncio.sleep(1) # คืนการควบคุม (Yield control) ระหว่างรอ
    print(f"{ctime()} -> [Chef] strains the noodle!")

async def bar_crew():
    print(f"{ctime()} -> [Bar] starts grinding coffee bean...")
    await asyncio.sleep(1) # คืนการควบคุม (Yield control) ระหว่างรอ
    print(f"{ctime()} -> [Bar] pours espresso shot!")

async def main():
    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())

    # การรอเพื่อให้มั่นใจว่าการจัดล็อกของทั้งสองงานพิมพ์ออกเสร็จสิ้นก่อนจบโปรแกรม
    await task_kitchen
    await task_bar

if __name__ == "__main__":
    asyncio.run(main())
