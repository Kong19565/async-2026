# Objective: Assignment 1 - The Smart Courier System
# ระบบส่งพัสดุด่วน: ฝึกการควบคุม Task และจัดการ CancelledError
import asyncio
from time import ctime

async def delivery_task(package_id, duration):
    try:
        # พิมพ์แจ้งเตือนตอนเริ่มส่งของ
        print(f"{ctime()} [{asyncio.current_task().get_name()}] Starting delivery for package {package_id}...")
        
        # จำลองการเดินทางของรถส่งของ
        await asyncio.sleep(duration)
        
        # ส่งของถึงมือลูกค้าสำเร็จก็ส่งสัญญาณบอกโปรแกรมหลัก
        return f"Package {package_id} Delivered!"
        
    except asyncio.CancelledError:
        # พอโดนสั่งดึงพนักงานกลับ ก็พิมพ์เคลียร์ของส่งคืนเข้าคลัง
        print(f"{ctime()} [{asyncio.current_task().get_name()}] Delivery Canceled! Returning package to warehouse.")
        # โยนข้อผิดพลาดเดิมกลับออกไปเพื่อให้สถานะตัวแปรภายนอกเปลี่ยนเป็น cancelled สมบูรณ์
        raise

async def main():
    # สร้าง Task ส่งของด่วนโดยตั้งชื่อว่า Express-Courier
    task = asyncio.create_task(delivery_task("P001", 5.0), name="Express-Courier")
    
    # ปล่อยให้ระบบเดินทางไปก่อน 2 วินาทีแรก
    await asyncio.sleep(2.0)
    
    # ตรวจเช็กสถานะการส่งของ
    print(f"{ctime()} [Main] Checking progress of task '{task.get_name()}': Done? -> {task.done()}")
    
    # พอเวลาผ่านไป 2 วินาทีแล้วงานยังไม่เสร็จ (เพราะตั้งไว้ 5 วินาที) ก็สั่งยกเลิกทันที
    if not task.done():
        print(f"{ctime()} [Main] Delivery is taking too long. Canceling the task...")
        task.cancel()
        
    # รอเคลียร์ผลลัพธ์สุดท้ายของ Task
    try:
        result = await task
        print(f"{ctime()} [Main] Result: {result}")
    except asyncio.CancelledError:
        # คาดการณ์ว่าต้องตกลงมาที่ข้อยกเว้นนี้เนื่องจากตัวงานโดนขัดจังหวะกลางทาง
        pass
        
    # ตรวจสอบสถานะภายนอกว่าตัวแปรเปลี่ยนเป็นยกเลิก (cancelled) เรียบร้อยหรือไม่
    print(f"{ctime()} [Main] Final task cancellation status: {task.cancelled()}")

if __name__ == "__main__":
    asyncio.run(main())
