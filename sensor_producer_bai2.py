import pika
import json
import random
import time
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    queue_name = "sensor_data_queue"
    channel.queue_declare(queue=queue_name)

    device_id = sys.argv[1] if len(sys.argv) > 1 else "sensor01"

    print(f" [*] Bắt đầu mô phỏng cảm biến {device_id}. Nhấn Ctrl+C để thoát.")

    try:
        while True:
            temperature = round(random.uniform(20.0, 45.0), 1)
            humidity = round(random.uniform(30.0, 70.0), 1)

            data = {
                "device_id": device_id,
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }

            message = json.dumps(data)

            channel.basic_publish(exchange="", routing_key=queue_name, body=message)

            print(f" [x] Đã gửi: {message}")

            time.sleep(3)
    except KeyboardInterrupt:
        print("\nĐã dừng mô phỏng cảm biến.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
