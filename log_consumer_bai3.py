import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    exchange_name = "iot_alert_exchange"
    channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

    queue_name = "log_queue"
    channel.queue_declare(queue=queue_name)

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key="#")

    print(
        " [*] Log Consumer đang chờ tin nhắn và ghi vào file logs.txt. Nhấn Ctrl+C để thoát."
    )

    def callback(ch, method, properties, body):
        log_msg = f"[{method.routing_key}] {body.decode()}"
        print(f" [log] {log_msg}")

        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(log_msg + "\n")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Đã dừng log consumer.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
