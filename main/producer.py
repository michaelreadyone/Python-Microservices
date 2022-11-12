
import pika, json

params = pika.URLParameters('amqps://adwqkwhe:fk_5Ufqi3MS4ouoO-8K_wXFtct-a9ymf@possum.lmq.cloudamqp.com/adwqkwhe')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print('boddy ', body)
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)