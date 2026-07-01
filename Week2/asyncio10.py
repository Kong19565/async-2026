# โปรแกรม 10: การดึงค่าผลลัพธ์กลับจากงาน (Return Values)
# Concept: การเรียกใช้ผลลัพธ์ที่รีเทิร์นกลับมาจาก Task ที่ทำงานเสร็จสิ้นแล้วด้วย .result() หรือกำหนดค่าโดยตรง
import asyncio

async def calculate_bill(customer, base_price):
    print(f"Calculating receipt for Customer {customer}...")
    await asyncio.sleep(1)
    final_price = base_price * 1.07 # คิดภาษี 7%
    return final_price

async def main():
    # จัดคิวการทำงานของคอร์รันทีนที่มีการรีเทิร์นค่ากลับมา
    task_a = asyncio.create_task(calculate_bill("A", 100))
    task_b = asyncio.create_task(calculate_bill("B", 200))

    # วิธีแรก: การรอ (await) ออบเจกต์และดึงผลลัพธ์การรีเทิร์นมาใช้งานโดยตรง
    result_a = await task_a
    result_b = await task_b

    # วิธีทางเลือก: ดึงค่าผ่านเมธอด .result() ภายหลังจากประมวลผลเสร็จสิ้น
    # result_b = task_b.result()

    print(f"\nFinal Bill A: {result_a:.2f}")
    print(f"Final Bill B: {result_b:.2f}")
    print(f"Combined Total Revenue: {result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
