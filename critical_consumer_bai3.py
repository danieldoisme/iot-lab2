import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    exchange_name = "iot_alert_exchange"
    channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

    queue_name = "critical_queue"
    channel.queue_declare(queue=queue_name)

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key="critical")

    print(" [*] Critical Consumer đang chờ message. Nhấn Ctrl+C để thoát.")

    def callback(ch, method, properties, body):
        print(f" [critical_queue] Đã nhận: {body.decode()}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Đã dừng critical consumer.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
