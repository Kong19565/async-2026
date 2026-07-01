# โปรแกรม 6: การสร้างงานแบบทำงานร่วมกัน (Concurrent Task)
# คอนเซปต์: การครอบคอร์รันทีนไว้ใน asyncio.create_task() เพื่อลงทะเบียนให้ประมวลผลใน Background
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start_time = time()

    # create_task() จะลงทะเบียนคอร์รันทีนลงในคิว Background ของ Event Loop ทันที
    task_a = asyncio.create_task(cook_spaghetti("A"))

    print(f"{ctime()} -> Main program can do other things while Task A runs in background.")

    # เรารอ (await) ออบเจกต์งานเพื่อให้มั่นใจว่าประมวลผลเสร็จสิ้นก่อน main() จะจบการทำงาน
    await task_a

    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
