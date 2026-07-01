# โปรแกรม 4: คีย์เวิร์ด await
# คอนเซปต์: การหยุดพักงานของคอร์รันทีนชั่วคราวเพื่อให้งานอื่นได้รันสลับโดยใช้ await
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    # การใช้งาน await เพื่อหยุดชั่วคราวและคืนการควบคุมให้กับ event loop
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}!")

async def main():
    start_time = time()
    print(f"{ctime()} -> Main: Starting to serve Customer A")
    await serve_customer("A")
    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
