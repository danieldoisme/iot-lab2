import pika
import json
import sys
import os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    queue_name = "sensor_data_queue"
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        try:
            data = json.loads(body.decode())

            device_id = data.get("device_id")
            temperature = data.get("temperature")
            humidity = data.get("humidity")

            print(f"Device: {device_id}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")

            if temperature > 35:
                print("CẢNH BÁO: Nhiệt độ cao")

            if humidity < 40:
                print("CẢNH BÁO: Độ ẩm thấp")

            print("-" * 20)

        except Exception as e:
            print(f"Lỗi khi xử lý message: {e}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(" [*] Monitor đang chạy. Nhấn Ctrl+C để thoát.")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Đã dừng monitor.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
