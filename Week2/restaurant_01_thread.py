# งานสัปดาห์ที่ 2: ระบบร้านอาหารแบบใช้ Threading
# คอนเซปต์: การทักทายลูกค้าแบบเรียงลำดับ ตามด้วยการใช้เธรดจัดการการรับออเดอร์/ทำอาหาร/มินิบาร์พร้อมกันแบบคู่ขนาน
import threading
from time import sleep, ctime, time

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Synchronous เรียงทีละคน
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการส่วนตัวของลูกค้าแต่ละคน ที่จะถูกนำไปรันแยกในเธรดของตัวเอง
def customer_private_workflow(customer):
    # รับออเดอร์
    print(f"{ctime()}  [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()}  [Thread-{customer}] Taking Order ...Done!")

    # ทำอาหาร
    print(f"{ctime()}  [Thread-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()}  [Thread-{customer}] Cooking Spaghetti ...Done!")

    # จัดการบาร์
    print(f"{ctime()}  [Thread-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()}  [Thread-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()}  [Thread-{customer}] All served!\n")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()

    # ----------------------------------------------------
    # เฟส 1: ต้อนรับลูกค้าหน้าร้านทีละคนแบบเรียงลำดับ
    # ----------------------------------------------------
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Threads! ---\n")

    # ----------------------------------------------------
    # เฟส 2: สร้างเธรดสำหรับขั้นตอนบริการคู่ขนาน
    # ----------------------------------------------------
    customer_threads = []
    for customer in customers:
        # สร้างเธรดแยกให้ลูกค้าแต่ละคน
        t = threading.Thread(target=customer_private_workflow, args=(customer,))
        customer_threads.append(t)
        t.start()

    # รอให้ลูกค้าทุกคนทำขั้นตอนทั้งหมดเสร็จสิ้น
    for t in customer_threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds.")
