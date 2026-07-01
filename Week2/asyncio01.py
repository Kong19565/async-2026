# โปรแกรม 1: ฟังก์ชัน Coroutine แรก
# คอนเซปต์: ทำความเข้าใจ async def และความแตกต่างจากฟังก์ชันปกติ
import inspect
from time import ctime

# ฟังก์ชันปกติ
def cook_spaghetti(customer):
    return f"Spaghetti for {customer}"

# ฟังก์ชัน Asynchronous (Coroutine function)
async def serve_customer(customer):
    return f"Served customer {customer}"

if __name__ == "__main__":
    # ตรวจสอบและพิมพ์ประเภท (types)
    print(f"{ctime()} -> type(cook_spaghetti): {type(cook_spaghetti)}")
    print(f"{ctime()} -> type(serve_customer): {type(serve_customer)}")

    # ตรวจสอบว่ามีสถานะเป็น coroutine function หรือไม่
    print(f"{ctime()} -> inspect.iscoroutinefunction(cook_spaghetti): {inspect.iscoroutinefunction(cook_spaghetti)}")
    print(f"{ctime()} -> inspect.iscoroutinefunction(serve_customer): {inspect.iscoroutinefunction(serve_customer)}")
