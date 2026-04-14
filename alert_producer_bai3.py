import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    exchange_name = "iot_alert_exchange"
    channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

    alerts = [
        ("info", "Hệ thống đang hoạt động bình thường"),
        ("warning", "Nhiệt độ phòng máy vượt ngưỡng warning"),
        ("critical", "Cảm biến kho lạnh mất kết nối critical"),
        ("warning", "Độ ẩm phòng server đang tăng cao"),
        ("critical", "Nguồn điện dự phòng gặp sự cố nghiêm trọng"),
    ]

    for severity, message in alerts:
        channel.basic_publish(
            exchange=exchange_name, routing_key=severity, body=message
        )
        print(f" [x] Đã gửi [{severity}]: {message}")

    connection.close()


if __name__ == "__main__":
    main()
