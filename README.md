# Bài tập AMQP (RabbitMQ) - Python
Họ tên: Đỗ Đức Thành
Mã SV: B21DCCN676

Dự án này bao gồm 3 bài tập minh họa việc sử dụng giao thức AMQP với Python thông qua thư viện `pika` và Broker RabbitMQ.

## Cấu hình Broker
- **Host**: `localhost` (Hoặc địa chỉ IP của RabbitMQ server)
- **Port**: `5672`
- **Username/Password**: `guest`/`guest` (Mặc định)

## Cài đặt và Chuẩn bị
1. Cài đặt `uv`: https://github.com/astral-sh/uv
2. Tạo Virtual Environment và cài đặt thư viện `pika`:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install pika
   ```

## Hướng dẫn chạy từng bài

### Bài 1: Gửi và nhận message cơ bản qua Queue
- **Terminal 1**: Chạy consumer để lắng nghe dữ liệu.
  ```bash
  python consumer_bai1.py
  ```
- **Terminal 2**: Chạy producer để gửi thông điệp. Bạn có thể nhập tin nhắn từ bàn phím.
  ```bash
  python producer_bai1.py
  ```

### Bài 2: Mô phỏng cảm biến IoT gửi dữ liệu (JSON)
- **Terminal 1**: Chạy monitor consumer.
  ```bash
  python monitor_consumer_bai2.py
  ```
- **Terminal 2, 3...**: Chạy nhiều sensor producer với các ID khác nhau.
  ```bash
  python sensor_producer_bai2.py sensor_A
  python sensor_producer_bai2.py sensor_B
  ```

### Bài 3: Hệ thống điều phối cảnh báo (Topic Exchange)
- **Terminal 1**: Chạy Log Consumer để ghi lại tất cả các mức cảnh báo vào file `logs.txt`.
  ```bash
  python log_consumer_bai3.py
  ```
- **Terminal 2**: Chạy Warning Consumer.
  ```bash
  python warning_consumer_bai3.py
  ```
- **Terminal 3**: Chạy Critical Consumer.
  ```bash
  python critical_consumer_bai3.py
  ```
- **Terminal 4**: Chạy Alert Producer.
  ```bash
  python alert_producer_bai3.py
  ```

## Kết quả đạt được

### Bài 1: Gửi và nhận message cơ bản
**Producer:**
```text
[*] Đã kết nối. Nhập nội dung để gửi hoặc 'exit' để thoát.
[x] Đã gửi mặc định: 'Xin chào từ ứng dụng Python AMQP - B21DCCN676 - Đỗ Đức Thành'
Nhập tin nhắn (hoặc 'exit'): Test tin nhắn số 2
[x] Đã gửi: 'Test tin nhắn số 2'
```
**Consumer:**
```text
[*] Đang chờ tin nhắn. Nhấn Ctrl+C để thoát.
Đã nhận message: Xin chào từ ứng dụng Python AMQP - B21DCCN676 - Đỗ Đức Thành
Thời gian nhận: 14:10:05
--------------------
Đã nhận message: Test tin nhắn số 2
Thời gian nhận: 14:10:15
--------------------
```

### Bài 2: Mô phỏng cảm biến IoT & Cảnh báo
**Sensor Producer:**
```text
[*] Bắt đầu mô phỏng cảm biến sensor_A. Nhấn Ctrl+C để thoát.
[x] Đã gửi: {"device_id": "sensor_A", "temperature": 36.2, "humidity": 38.5, "timestamp": "2026-04-14 14:11:00"}
```
**Monitor Consumer:**
```text
Device: sensor_A
Temperature: 36.2
Humidity: 38.5
CẢNH BÁO: Nhiệt độ cao
CẢNH BÁO: Độ ẩm thấp
--------------------
```

### Bài 3: Điều phối cảnh báo với Topic Exchange
**Alert Producer:**
```text
[x] Đã gửi [info]: Hệ thống đang hoạt động bình thường
[x] Đã gửi [warning]: Nhiệt độ phòng máy vượt ngưỡng warning
[x] Đã gửi [critical]: Cảm biến kho lạnh mất kết nối critical
```
**Warning Consumer:**
```text
[*] Warning Consumer đang chờ message. Nhấn Ctrl+C để thoát.
[warning_queue] Đã nhận: Nhiệt độ phòng máy vượt ngưỡng warning
```
**Log Consumer (Nhận tất cả):**
```text
[log] [info] Hệ thống đang hoạt động bình thường
[log] [warning] Nhiệt độ phòng máy vượt ngưỡng warning
[log] [critical] Cảm biến kho lạnh mất kết nối critical
```