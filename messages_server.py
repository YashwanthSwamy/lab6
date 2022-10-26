from concurrent import futures
import logging

import io
from PIL import Image
import grpc
import base64

import messages_pb2
import messages_pb2_grpc

def process_raw_img(data):
    ioBuffer = io.BytesIO(data)
    img = Image.open(ioBuffer)
    return {
        'width' : int(img.size[0]),
        'height' : int(img.size[1])
        }

def process_json_img(data):
    imgdata = base64.b64decode(data)
    im = Image.open(io.BytesIO(imgdata))
    print(im.size)
    width, height = im.size
    return {
        'width' : int(width),
        'height' : int(height)
        }

def process_dot_product(list_1, list_2):
    res = []
    for l1, l2 in zip(list_1, list_2):
        res.append(l1 * l2)
    return res

class Lab_6(messages_pb2_grpc.Lab_6Servicer):

    def add(self, request, context):
        a, b = request.a, request.b
        print(f"Received add request {a} {b}")
        return messages_pb2.addMsgReply(sum=a + b)
    
    def rawimage(self, request, context):
        print(f"Received Raw Image request")
        res = process_raw_img(request.img)
        width, height = res["width"], res["height"]
        return messages_pb2.rawImageMsgReply(width= width, height= height)
    
    def dotproduct(self, request, context):
        print(f"Received Dot Product request")
        resp = process_dot_product(request.a, request.b)
        return messages_pb2.dotProductMsgReply(dotProductSum=resp)
    
    def jsonimage(self, request, context):
        print(f"Received Json Image request")
        res = process_json_img(request.img)
        width, height = res["width"], res["height"]
        return messages_pb2.jsonImageMsgReply(width= width, height= height)


def serve():
    port = '5000'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_Lab_6Servicer_to_server(Lab_6(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()