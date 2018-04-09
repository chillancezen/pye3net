# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import common_pb2 as common__pb2
import vswitch_lanzone_pb2 as vswitch__lanzone__pb2


class vswitch_lanzoneStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.rpc_get_vswitch_lanzone = channel.unary_unary(
        '/vswitch_lanzone/rpc_get_vswitch_lanzone',
        request_serializer=vswitch__lanzone__pb2.req_lanzone_key.SerializeToString,
        response_deserializer=vswitch__lanzone__pb2.res_vswitch_lanzone.FromString,
        )
    self.rpc_list_vswitch_lanzones = channel.stream_stream(
        '/vswitch_lanzone/rpc_list_vswitch_lanzones',
        request_serializer=vswitch__lanzone__pb2.req_lanzone_key.SerializeToString,
        response_deserializer=vswitch__lanzone__pb2.res_vswitch_lanzone.FromString,
        )
    self.rpc_register_vswitch_lanzone = channel.unary_unary(
        '/vswitch_lanzone/rpc_register_vswitch_lanzone',
        request_serializer=vswitch__lanzone__pb2.res_vswitch_lanzone.SerializeToString,
        response_deserializer=vswitch__lanzone__pb2.res_vswitch_lanzone.FromString,
        )
    self.rpc_unregister_vswitch_lanzone = channel.unary_unary(
        '/vswitch_lanzone/rpc_unregister_vswitch_lanzone',
        request_serializer=vswitch__lanzone__pb2.req_lanzone_key.SerializeToString,
        response_deserializer=common__pb2.null.FromString,
        )
    self.rpc_update_vswitch_lanzone = channel.unary_unary(
        '/vswitch_lanzone/rpc_update_vswitch_lanzone',
        request_serializer=vswitch__lanzone__pb2.res_vswitch_lanzone.SerializeToString,
        response_deserializer=common__pb2.null.FromString,
        )


class vswitch_lanzoneServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def rpc_get_vswitch_lanzone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def rpc_list_vswitch_lanzones(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def rpc_register_vswitch_lanzone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def rpc_unregister_vswitch_lanzone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def rpc_update_vswitch_lanzone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_vswitch_lanzoneServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'rpc_get_vswitch_lanzone': grpc.unary_unary_rpc_method_handler(
          servicer.rpc_get_vswitch_lanzone,
          request_deserializer=vswitch__lanzone__pb2.req_lanzone_key.FromString,
          response_serializer=vswitch__lanzone__pb2.res_vswitch_lanzone.SerializeToString,
      ),
      'rpc_list_vswitch_lanzones': grpc.stream_stream_rpc_method_handler(
          servicer.rpc_list_vswitch_lanzones,
          request_deserializer=vswitch__lanzone__pb2.req_lanzone_key.FromString,
          response_serializer=vswitch__lanzone__pb2.res_vswitch_lanzone.SerializeToString,
      ),
      'rpc_register_vswitch_lanzone': grpc.unary_unary_rpc_method_handler(
          servicer.rpc_register_vswitch_lanzone,
          request_deserializer=vswitch__lanzone__pb2.res_vswitch_lanzone.FromString,
          response_serializer=vswitch__lanzone__pb2.res_vswitch_lanzone.SerializeToString,
      ),
      'rpc_unregister_vswitch_lanzone': grpc.unary_unary_rpc_method_handler(
          servicer.rpc_unregister_vswitch_lanzone,
          request_deserializer=vswitch__lanzone__pb2.req_lanzone_key.FromString,
          response_serializer=common__pb2.null.SerializeToString,
      ),
      'rpc_update_vswitch_lanzone': grpc.unary_unary_rpc_method_handler(
          servicer.rpc_update_vswitch_lanzone,
          request_deserializer=vswitch__lanzone__pb2.res_vswitch_lanzone.FromString,
          response_serializer=common__pb2.null.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'vswitch_lanzone', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))