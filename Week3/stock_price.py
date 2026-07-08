import asyncio
from time import ctime

# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)

async def fetch_stock_price(server_name, delay):
    # จำลองความล่าช้าในการดึงข้อมูลจากอินเทอร์เน็ตของแต่ละสาขา
    await asyncio.sleep(delay)
    # ส่งข้อความผลลัพธ์ราคาหุ้นกลับไปเมื่ออ่านข้อมูลสำเร็จ
    return f"[{server_name}] Price: 150 USD"

async def main():
    # แตก Task รันแข่งพร้อมกันทั้ง 3 สาขา และสแตนด์บายใน Event Loop
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0), name="Server-Alpha"),
        asyncio.create_task(fetch_stock_price("Beta", 0.8), name="Server-Beta"),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5), name="Server-Gamma")
    }
    
    # สั่งให้โปรแกรมหลุดจากการรอทันทีที่เซิร์ฟเวอร์ย่อยตัวแรกส่งข้อมูลกลับมาสำเร็จ
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # วนลูปเอาผลลัพธ์ของตัวที่ชนะมาพิมพ์โชว์ทางหน้าจอ
    for finished_task in done:
        print(f"{ctime()} [Main] Winner result: {finished_task.result()}")
        
    # ปิดกั้นทรัพยากรตัวที่เหลือทั้งหมดที่ประมวลผลช้ากว่า เพื่อลดโอกาสรั่วไหลของหน่วยความจำ
    for ongoing_task in pending:
        print(f"{ctime()} [Main] Canceling pending task: {ongoing_task.get_name()}")
        ongoing_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
