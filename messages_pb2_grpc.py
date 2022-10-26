# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class Lab_6Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add = channel.unary_unary(
                '/lab_6.Lab_6/add',
                request_serializer=messages__pb2.addMsg.SerializeToString,
                response_deserializer=messages__pb2.addMsgReply.FromString,
                )
        self.rawimage = channel.unary_unary(
                '/lab_6.Lab_6/rawimage',
                request_serializer=messages__pb2.rawImageMsg.SerializeToString,
                response_deserializer=messages__pb2.rawImageMsgReply.FromString,
                )
        self.dotproduct = channel.unary_unary(
                '/lab_6.Lab_6/dotproduct',
                request_serializer=messages__pb2.dotProductMsg.SerializeToString,
                response_deserializer=messages__pb2.dotProductMsgReply.FromString,
                )
        self.jsonimage = channel.unary_unary(
                '/lab_6.Lab_6/jsonimage',
                request_serializer=messages__pb2.jsonImageMsg.SerializeToString,
                response_deserializer=messages__pb2.jsonImageMsgReply.FromString,
                )


class Lab_6Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rawimage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dotproduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def jsonimage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Lab_6Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=messages__pb2.addMsg.FromString,
                    response_serializer=messages__pb2.addMsgReply.SerializeToString,
            ),
            'rawimage': grpc.unary_unary_rpc_method_handler(
                    servicer.rawimage,
                    request_deserializer=messages__pb2.rawImageMsg.FromString,
                    response_serializer=messages__pb2.rawImageMsgReply.SerializeToString,
            ),
            'dotproduct': grpc.unary_unary_rpc_method_handler(
                    servicer.dotproduct,
                    request_deserializer=messages__pb2.dotProductMsg.FromString,
                    response_serializer=messages__pb2.dotProductMsgReply.SerializeToString,
            ),
            'jsonimage': grpc.unary_unary_rpc_method_handler(
                    servicer.jsonimage,
                    request_deserializer=messages__pb2.jsonImageMsg.FromString,
                    response_serializer=messages__pb2.jsonImageMsgReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lab_6.Lab_6', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lab_6(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab_6.Lab_6/add',
            messages__pb2.addMsg.SerializeToString,
            messages__pb2.addMsgReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rawimage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab_6.Lab_6/rawimage',
            messages__pb2.rawImageMsg.SerializeToString,
            messages__pb2.rawImageMsgReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dotproduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab_6.Lab_6/dotproduct',
            messages__pb2.dotProductMsg.SerializeToString,
            messages__pb2.dotProductMsgReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def jsonimage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab_6.Lab_6/jsonimage',
            messages__pb2.jsonImageMsg.SerializeToString,
            messages__pb2.jsonImageMsgReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
