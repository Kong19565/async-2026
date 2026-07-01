# โปรแกรม 2: ออบเจกต์ Coroutine
# คอนเซปต์: การเรียกใช้ฟังก์ชัน async def จะเป็นการสร้าง "Object" แต่ยังไม่ประมวลผลทันที
import asyncio
import inspect
from time import ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}!")

if __name__ == "__main__":
    print(f"{ctime()} -> Calling serve_customer('A')...")
    # การเรียกฟังก์ชัน coroutine จะสร้างออบเจกต์ coroutine ขึ้นมา
    coro = serve_customer("A")
    print(f"{ctime()} -> Coroutine object created: {coro}")
    print(f"{ctime()} -> (หมายเหตุ: ข้อความ 'Cooking for A...' ยังไม่พิมพ์ออกมาเนื่องจากยังไม่ได้สั่งรัน)")

    # ตรวจสอบประเภทและสถานะของออบเจกต์ coroutine
    print(f"{ctime()} -> type(coro): {type(coro)}")
    print(f"{ctime()} -> inspect.iscoroutine(coro): {inspect.iscoroutine(coro)}")
