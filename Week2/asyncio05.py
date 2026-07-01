# โปรแกรม 5: การทำงานแบบเรียงลำดับ (วิธีที่ผิด)
# คอนเซปต์: แสดงให้เห็นว่าการใช้ await รันงานเรียงทีละงานจะยังเป็นกระบวนการแบบเรียงลำดับ (Synchronous)
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}!")

async def main():
    start = time()
    # หากกดสั่งรอ (await) ทีละตัว มันจะทำงานเป็นลำดับทีละคนตามเดิม!
    await serve_customer("A")
    await serve_customer("B")

    print(f"Total Time: {time() - start:.2f} seconds") # จะใช้เวลาประมาณ 2 วินาที

if __name__ == "__main__":
    asyncio.run(main())
