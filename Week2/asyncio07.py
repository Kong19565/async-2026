# โปรแกรม 7: การทำงานคู่ขนานของงานสองงาน (Dual Tasks Concurrency)
# คอนเซปต์: การจัดคิวการทำงานคู่ขนานกันของสองงานแยกอิสระและสั่งรอทีละตัวโดยไม่ใช้ gather
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    # ลงทะเบียนงานทั้งสองตัวเข้า Event Loop ทันทีเพื่อรันคู่ขนาน
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))

    # การรอ (await) task_a จะเปิดโอกาสให้ task_b ทำงานควบคู่กันไประหว่างสลีปของ task_a
    await task_a
    await task_b

    # เวลารวมลดลงเหลือประมาณ 1 วินาทีเนื่องจากรันคู่ขนานกัน!
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
