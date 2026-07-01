# งานสัปดาห์ที่ 2: ระบบร้านอาหารแบบใช้ Asyncio
# คอนเซปต์: การทักทายลูกค้าแบบเรียงลำดับ ตามด้วยการใช้ Task ของ Asyncio จัดการการรับออเดอร์/ทำอาหาร/มินิบาร์พร้อมกันแบบคู่ขนาน
import asyncio
from time import time, ctime

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Synchronous เรียงทีละคน
async def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการส่วนตัวของลูกค้าแต่ละคน ที่จะถูกนำไปรันแยกใน Task ของตัวเอง
async def customer_private_workflow(customer):
    # รับออเดอร์
    print(f"{ctime()}  [Task-{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()}  [Task-{customer}] Taking Order ...Done!")

    # ทำอาหาร
    print(f"{ctime()}  [Task-{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()}  [Task-{customer}] Cooking Spaghetti ...Done!")

    # จัดการบาร์
    print(f"{ctime()}  [Task-{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()}  [Task-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()}  [Task-{customer}] All served!\n")

async def main():
    start_time = time()
    customers = ['A', 'B', 'C']

    # ----------------------------------------------------
    # เฟส 1: ต้อนรับลูกค้าหน้าร้านทีละคนแบบเรียงลำดับ
    # ----------------------------------------------------
    for customer in customers:
        await greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Async Tasks! ---\n")

    # ----------------------------------------------------
    # เฟส 2: สร้างและรัน Task สำหรับขั้นตอนบริการคู่ขนาน
    # ----------------------------------------------------
    tasks = []
    for customer in customers:
        task = asyncio.create_task(customer_private_workflow(customer))
        tasks.append(task)

    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())
