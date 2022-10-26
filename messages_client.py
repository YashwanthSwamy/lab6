from __future__ import print_function
# import imp
# import json
import time
import sys
import grpc
import base64

import messages_pb2
import messages_pb2_grpc

import random

def add(stub, debug=False):
    data = messages_pb2.addMsg(a=10, b=20)
    resp=stub.add(data)
    if debug:
        print(f"Add Response sum: {resp.sum}")

def rawimage(stub, debug=False):
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    data = messages_pb2.rawImageMsg(img=img)
    resp=stub.rawimage(data)
    if debug:
        print(f"Raw Image Response width: {resp.width} height: {resp.height}")
    
def dotproduct(stub, debug=False):
    """
    dot product
    """
    data = messages_pb2.dotProductMsg()
    data.a.extend([random.random() for x in range(10)])
    data.b.extend([random.random() for x in range(10)])
    resp=stub.dotproduct(data)
    if debug:
        print(f" Dot Product Response : {resp.dotProductSum}")

def jsonimage(stub, debug=False):
    """
    json image
    """
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    encoded_img = base64.b64encode(img)
    data = messages_pb2.jsonImageMsg(img=encoded_img)
    resp=stub.jsonimage(data)
    if debug:
        print(f"Raw Image Response width: {resp.width} height: {resp.height}")

if len(sys.argv) < 3:
    print(f"missing arguments sample command '{sys.argv[0]} <server-ip> <method> <repitition>'")
    print("method - add, rawImage, dotProduct, jsonImage")

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])

with grpc.insecure_channel(host) as channel:
    stub = messages_pb2_grpc.Lab_6Stub(channel)
    print(f"Running {reps} reps")

    if cmd == 'rawImage':
        start = time.perf_counter()
        for x in range(reps):
            rawimage(stub, debug=True)
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'add':
        start = time.perf_counter()
        for x in range(reps):
            add(stub, debug=True)
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'jsonImage':
        start = time.perf_counter()
        for x in range(reps):
            jsonimage(stub, debug=True)
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'dotProduct':
        start = time.perf_counter()
        for x in range(reps):
            dotproduct(stub, debug=True)
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    else:
        print("Unknown option", cmd)