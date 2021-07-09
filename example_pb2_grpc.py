# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2


class AgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HandleMessage = channel.unary_unary(
                '/Agent/HandleMessage',
                request_serializer=example__pb2.RequestMessage.SerializeToString,
                response_deserializer=example__pb2.RequestMessage.FromString,
                )


class AgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HandleMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HandleMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleMessage,
                    request_deserializer=example__pb2.RequestMessage.FromString,
                    response_serializer=example__pb2.RequestMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HandleMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Agent/HandleMessage',
            example__pb2.RequestMessage.SerializeToString,
            example__pb2.RequestMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
