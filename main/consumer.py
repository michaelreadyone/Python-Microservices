import pika, json

params = pika.URLParameters('amqps://adwqkwhe:fk_5Ufqi3MS4ouoO-8K_wXFtct-a9ymf@possum.lmq.cloudamqp.com/adwqkwhe')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()