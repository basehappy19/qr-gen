import qrcode
import os
import uuid

# 1. สร้างโฟลเดอร์ 'outputs' ถ้ายังไม่มี
output_dir = "outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# 2. รับอินพุตจากผู้ใช้งาน
data = input("Enter the URL or text you want to convert to QR Code: ")

if data.strip():
    # 3. สุ่มชื่อไฟล์ด้วย UUID และกำหนด Path ไปที่โฟลเดอร์ outputs
    random_filename = f"{uuid.uuid4().hex[:8]}.png"
    file_path = os.path.join(output_dir, random_filename)

    # 4. สร้างและบันทึก QR Code
    img = qrcode.make(data)
    img.save(file_path)

    print("-" * 30)
    print(f"✅ Success!")
    print(f"🔗 Data: {data}")
    print(f"📁 Saved to: {file_path}")
    print("-" * 30)
else:
    print("❌ Error: Please enter some data.")