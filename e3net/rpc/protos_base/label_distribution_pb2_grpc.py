# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import common_pb2 as common__pb2
import label_distribution_pb2 as label__distribution__pb2


class label_distributionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.rpc_deposit_labels = channel.stream_unary(
        '/label_distribution/rpc_deposit_labels',
        request_serializer=label__distribution__pb2.label_request.SerializeToString,
        response_deserializer=common__pb2.null.FromString,
        )
    self.rpc_withdraw_labels = channel.stream_unary(
        '/label_distribution/rpc_withdraw_labels',
        request_serializer=label__distribution__pb2.label_request.SerializeToString,
        response_deserializer=common__pb2.null.FromString,
        )
    self.rpc_pull_labels = channel.stream_stream(
        '/label_distribution/rpc_pull_labels',
        request_serializer=label__distribution__pb2.label_request.SerializeToString,
        response_deserializer=label__distribution__pb2.label_response.FromString,
        )


class label_distributionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def rpc_deposit_labels(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def rpc_withdraw_labels(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def rpc_pull_labels(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_label_distributionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'rpc_deposit_labels': grpc.stream_unary_rpc_method_handler(
          servicer.rpc_deposit_labels,
          request_deserializer=label__distribution__pb2.label_request.FromString,
          response_serializer=common__pb2.null.SerializeToString,
      ),
      'rpc_withdraw_labels': grpc.stream_unary_rpc_method_handler(
          servicer.rpc_withdraw_labels,
          request_deserializer=label__distribution__pb2.label_request.FromString,
          response_serializer=common__pb2.null.SerializeToString,
      ),
      'rpc_pull_labels': grpc.stream_stream_rpc_method_handler(
          servicer.rpc_pull_labels,
          request_deserializer=label__distribution__pb2.label_request.FromString,
          response_serializer=label__distribution__pb2.label_response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'label_distribution', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
