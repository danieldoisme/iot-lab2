import pika
import sys
import os
from datetime import datetime


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    queue_name = "iot_lab_queue"
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        message = body.decode()
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Đã nhận message: {message}")
        print(f"Thời gian nhận: {current_time}")
        print("-" * 20)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(" [*] Đang chờ tin nhắn. Nhấn Ctrl+C để thoát.")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Đã dừng consumer.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
