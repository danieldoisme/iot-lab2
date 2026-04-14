import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    queue_name = "iot_lab_queue"
    channel.queue_declare(queue=queue_name)

    print(" [*] Đã kết nối. Nhập nội dung để gửi hoặc 'exit' để thoát.")

    try:
        default_msg = "Xin chào từ ứng dụng Python AMQP - B21DCCN676 - Đỗ Đức Thành"
        channel.basic_publish(exchange="", routing_key=queue_name, body=default_msg)
        print(f" [x] Đã gửi mặc định: '{default_msg}'")

        while True:
            msg = input("Nhập tin nhắn (hoặc 'exit'): ")
            if msg.lower() == "exit":
                break
            if not msg:
                continue

            channel.basic_publish(exchange="", routing_key=queue_name, body=msg)
            print(f" [x] Đã gửi: '{msg}'")

    except KeyboardInterrupt:
        print("\nĐã dừng producer.")
    finally:
        connection.close()
        print("Đã đóng kết nối.")


if __name__ == "__main__":
    main()
