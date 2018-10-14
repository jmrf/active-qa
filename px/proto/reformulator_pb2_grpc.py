# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import reformulator_pb2 as reformulator__pb2


class ReformulatorServerStub(object):
  """gRPC service for the reformulator server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetReformulations = channel.unary_unary(
        '/active_qa.ReformulatorServer/GetReformulations',
        request_serializer=reformulator__pb2.ReformulatorRequest.SerializeToString,
        response_deserializer=reformulator__pb2.ReformulatorResponse.FromString,
        )
    self.Train = channel.unary_unary(
        '/active_qa.ReformulatorServer/Train',
        request_serializer=reformulator__pb2.TrainingRequest.SerializeToString,
        response_deserializer=reformulator__pb2.TrainingResponse.FromString,
        )
    self.SaveTrieToFile = channel.unary_unary(
        '/active_qa.ReformulatorServer/SaveTrieToFile',
        request_serializer=reformulator__pb2.SaveTrieToFileRequest.SerializeToString,
        response_deserializer=reformulator__pb2.SaveTrieToFileResponse.FromString,
        )
    self.LoadTrieFromFile = channel.unary_unary(
        '/active_qa.ReformulatorServer/LoadTrieFromFile',
        request_serializer=reformulator__pb2.LoadTrieFromFileRequest.SerializeToString,
        response_deserializer=reformulator__pb2.LoadTrieFromFileResponse.FromString,
        )
    self.UpdateTrie = channel.unary_unary(
        '/active_qa.ReformulatorServer/UpdateTrie',
        request_serializer=reformulator__pb2.UpdateTrieRequest.SerializeToString,
        response_deserializer=reformulator__pb2.UpdateTrieResponse.FromString,
        )


class ReformulatorServerServicer(object):
  """gRPC service for the reformulator server.
  """

  def GetReformulations(self, request, context):
    """The request contains a list of questions and the response contains a list
    of list of reformulations.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Train(self, request, context):
    """Performs a supervised update of the model, using weighted training
    examples.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveTrieToFile(self, request, context):
    """Saves the trie to a file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LoadTrieFromFile(self, request, context):
    """Loads the trie from a file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTrie(self, request, context):
    """Updates the trie.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReformulatorServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetReformulations': grpc.unary_unary_rpc_method_handler(
          servicer.GetReformulations,
          request_deserializer=reformulator__pb2.ReformulatorRequest.FromString,
          response_serializer=reformulator__pb2.ReformulatorResponse.SerializeToString,
      ),
      'Train': grpc.unary_unary_rpc_method_handler(
          servicer.Train,
          request_deserializer=reformulator__pb2.TrainingRequest.FromString,
          response_serializer=reformulator__pb2.TrainingResponse.SerializeToString,
      ),
      'SaveTrieToFile': grpc.unary_unary_rpc_method_handler(
          servicer.SaveTrieToFile,
          request_deserializer=reformulator__pb2.SaveTrieToFileRequest.FromString,
          response_serializer=reformulator__pb2.SaveTrieToFileResponse.SerializeToString,
      ),
      'LoadTrieFromFile': grpc.unary_unary_rpc_method_handler(
          servicer.LoadTrieFromFile,
          request_deserializer=reformulator__pb2.LoadTrieFromFileRequest.FromString,
          response_serializer=reformulator__pb2.LoadTrieFromFileResponse.SerializeToString,
      ),
      'UpdateTrie': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTrie,
          request_deserializer=reformulator__pb2.UpdateTrieRequest.FromString,
          response_serializer=reformulator__pb2.UpdateTrieResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'active_qa.ReformulatorServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
