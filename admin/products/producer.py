import pika, json

params = pika.URLParameters('amqps://adwqkwhe:fk_5Ufqi3MS4ouoO-8K_wXFtct-a9ymf@possum.lmq.cloudamqp.com/adwqkwhe')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='helloo')

# def publish(method, body):
#     properties = pika.BasicProperties(method)
#     channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)