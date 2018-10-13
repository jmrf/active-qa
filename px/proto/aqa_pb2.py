# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aqa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aqa.proto',
  package='active_qa',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\taqa.proto\x12\tactive_qa\"7\n\x07\x43ontext\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12\x1a\n\x12tokenized_document\x18\x02 \x03(\t\"\xab\x02\n\x05Query\x12\x10\n\x08question\x18\x01 \x01(\t\x12$\n\x08\x63ontexts\x18\x02 \x03(\x0b\x32\x12.active_qa.Context\x12\n\n\x02id\x18\x03 \x01(\t\x12\x41\n\x11passthrough_debug\x18\x04 \x03(\x0b\x32&.active_qa.Query.PassthroughDebugEntry\x12\x1a\n\x12tokenized_question\x18\x05 \x03(\t\x12\x19\n\x11original_question\x18\x06 \x01(\t\x12\x15\n\ris_impossible\x18\x07 \x01(\x08\x12\x14\n\x0csecondary_id\x18\x08 \x01(\t\x1a\x37\n\x15PassthroughDebugEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x89\x01\n\x0bObservation\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x32\n\x06scores\x18\x02 \x03(\x0b\x32\".active_qa.Observation.ScoresEntry\x1a-\n\x0bScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"\xce\x03\n\x08Response\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x1a\n\x12processed_question\x18\x02 \x01(\t\x12\'\n\x07\x61nswers\x18\x03 \x03(\x0b\x32\x16.active_qa.Observation\x12;\n\x0cobservations\x18\x04 \x03(\x0b\x32%.active_qa.Response.ObservationsEntry\x12\n\n\x02id\x18\x05 \x01(\t\x12\x44\n\x11passthrough_debug\x18\x06 \x03(\x0b\x32).active_qa.Response.PassthroughDebugEntry\x12\x19\n\x11original_question\x18\x07 \x01(\t\x12\x15\n\rerror_message\x18\x08 \x01(\t\x12$\n\x1cquestion_original_similarity\x18\t \x01(\x01\x1aK\n\x11ObservationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.active_qa.Observation:\x02\x38\x01\x1a\x37\n\x15PassthroughDebugEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n\x12\x45nvironmentRequest\x12!\n\x07queries\x18\x01 \x03(\x0b\x32\x10.active_qa.Query\"=\n\x13\x45nvironmentResponse\x12&\n\tresponses\x18\x01 \x03(\x0b\x32\x13.active_qa.Response\"W\n\rQueryResponse\x12\x1f\n\x05query\x18\x01 \x01(\x0b\x32\x10.active_qa.Query\x12%\n\x08response\x18\x02 \x01(\x0b\x32\x13.active_qa.Response\"\xf8\x01\n\nQAInstance\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\x0bqr_original\x18\x02 \x01(\x0b\x32\x18.active_qa.QueryResponse\x12-\n\x0bqr_rewrites\x18\x03 \x03(\x0b\x32\x18.active_qa.QueryResponse\x12\x14\n\x0cgold_answers\x18\x04 \x03(\t\x12)\n\x07qr_best\x18\x05 \x01(\x0b\x32\x18.active_qa.QueryResponse\x12\x15\n\ris_impossible\x18\x06 \x01(\x08\x12\x19\n\x11plausible_answers\x18\x07 \x03(\t\x12\r\n\x05title\x18\x08 \x01(\t*P\n\tErrorCode\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x0e\n\nNO_QUERIES\x10\x01\x12\x12\n\x0e\x45MPTY_QUESTION\x10\x02\x12\x11\n\rSCRAPE_FAILED\x10\x03\x32g\n\x11\x45nvironmentServer\x12R\n\x0fGetObservations\x12\x1d.active_qa.EnvironmentRequest\x1a\x1e.active_qa.EnvironmentResponse\"\x00')
)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='active_qa.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_QUERIES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY_QUESTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRAPE_FAILED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1448,
  serialized_end=1528,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
NO_ERROR = 0
NO_QUERIES = 1
EMPTY_QUESTION = 2
SCRAPE_FAILED = 3



_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='active_qa.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='active_qa.Context.document', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenized_document', full_name='active_qa.Context.tokenized_document', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=79,
)


_QUERY_PASSTHROUGHDEBUGENTRY = _descriptor.Descriptor(
  name='PassthroughDebugEntry',
  full_name='active_qa.Query.PassthroughDebugEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='active_qa.Query.PassthroughDebugEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='active_qa.Query.PassthroughDebugEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=381,
)

_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='active_qa.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='active_qa.Query.question', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contexts', full_name='active_qa.Query.contexts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='active_qa.Query.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passthrough_debug', full_name='active_qa.Query.passthrough_debug', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokenized_question', full_name='active_qa.Query.tokenized_question', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_question', full_name='active_qa.Query.original_question', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_impossible', full_name='active_qa.Query.is_impossible', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_id', full_name='active_qa.Query.secondary_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_QUERY_PASSTHROUGHDEBUGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=381,
)


_OBSERVATION_SCORESENTRY = _descriptor.Descriptor(
  name='ScoresEntry',
  full_name='active_qa.Observation.ScoresEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='active_qa.Observation.ScoresEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='active_qa.Observation.ScoresEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=510,
)

_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='active_qa.Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='active_qa.Observation.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scores', full_name='active_qa.Observation.scores', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OBSERVATION_SCORESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10000, 536870912), ],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=521,
)


_RESPONSE_OBSERVATIONSENTRY = _descriptor.Descriptor(
  name='ObservationsEntry',
  full_name='active_qa.Response.ObservationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='active_qa.Response.ObservationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='active_qa.Response.ObservationsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=929,
)

_RESPONSE_PASSTHROUGHDEBUGENTRY = _descriptor.Descriptor(
  name='PassthroughDebugEntry',
  full_name='active_qa.Response.PassthroughDebugEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='active_qa.Response.PassthroughDebugEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='active_qa.Response.PassthroughDebugEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=381,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='active_qa.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='active_qa.Response.question', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed_question', full_name='active_qa.Response.processed_question', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answers', full_name='active_qa.Response.answers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observations', full_name='active_qa.Response.observations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='active_qa.Response.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passthrough_debug', full_name='active_qa.Response.passthrough_debug', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_question', full_name='active_qa.Response.original_question', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='active_qa.Response.error_message', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='question_original_similarity', full_name='active_qa.Response.question_original_similarity', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_OBSERVATIONSENTRY, _RESPONSE_PASSTHROUGHDEBUGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=986,
)


_ENVIRONMENTREQUEST = _descriptor.Descriptor(
  name='EnvironmentRequest',
  full_name='active_qa.EnvironmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queries', full_name='active_qa.EnvironmentRequest.queries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=988,
  serialized_end=1043,
)


_ENVIRONMENTRESPONSE = _descriptor.Descriptor(
  name='EnvironmentResponse',
  full_name='active_qa.EnvironmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='active_qa.EnvironmentResponse.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1045,
  serialized_end=1106,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='active_qa.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='active_qa.QueryResponse.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='active_qa.QueryResponse.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1108,
  serialized_end=1195,
)


_QAINSTANCE = _descriptor.Descriptor(
  name='QAInstance',
  full_name='active_qa.QAInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='active_qa.QAInstance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qr_original', full_name='active_qa.QAInstance.qr_original', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qr_rewrites', full_name='active_qa.QAInstance.qr_rewrites', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gold_answers', full_name='active_qa.QAInstance.gold_answers', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qr_best', full_name='active_qa.QAInstance.qr_best', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_impossible', full_name='active_qa.QAInstance.is_impossible', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plausible_answers', full_name='active_qa.QAInstance.plausible_answers', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='active_qa.QAInstance.title', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1198,
  serialized_end=1446,
)

_QUERY_PASSTHROUGHDEBUGENTRY.containing_type = _QUERY
_QUERY.fields_by_name['contexts'].message_type = _CONTEXT
_QUERY.fields_by_name['passthrough_debug'].message_type = _QUERY_PASSTHROUGHDEBUGENTRY
_OBSERVATION_SCORESENTRY.containing_type = _OBSERVATION
_OBSERVATION.fields_by_name['scores'].message_type = _OBSERVATION_SCORESENTRY
_RESPONSE_OBSERVATIONSENTRY.fields_by_name['value'].message_type = _OBSERVATION
_RESPONSE_OBSERVATIONSENTRY.containing_type = _RESPONSE
_RESPONSE_PASSTHROUGHDEBUGENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['answers'].message_type = _OBSERVATION
_RESPONSE.fields_by_name['observations'].message_type = _RESPONSE_OBSERVATIONSENTRY
_RESPONSE.fields_by_name['passthrough_debug'].message_type = _RESPONSE_PASSTHROUGHDEBUGENTRY
_ENVIRONMENTREQUEST.fields_by_name['queries'].message_type = _QUERY
_ENVIRONMENTRESPONSE.fields_by_name['responses'].message_type = _RESPONSE
_QUERYRESPONSE.fields_by_name['query'].message_type = _QUERY
_QUERYRESPONSE.fields_by_name['response'].message_type = _RESPONSE
_QAINSTANCE.fields_by_name['qr_original'].message_type = _QUERYRESPONSE
_QAINSTANCE.fields_by_name['qr_rewrites'].message_type = _QUERYRESPONSE
_QAINSTANCE.fields_by_name['qr_best'].message_type = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['EnvironmentRequest'] = _ENVIRONMENTREQUEST
DESCRIPTOR.message_types_by_name['EnvironmentResponse'] = _ENVIRONMENTRESPONSE
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['QAInstance'] = _QAINSTANCE
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.Context)
  ))
_sym_db.RegisterMessage(Context)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(

  PassthroughDebugEntry = _reflection.GeneratedProtocolMessageType('PassthroughDebugEntry', (_message.Message,), dict(
    DESCRIPTOR = _QUERY_PASSTHROUGHDEBUGENTRY,
    __module__ = 'aqa_pb2'
    # @@protoc_insertion_point(class_scope:active_qa.Query.PassthroughDebugEntry)
    ))
  ,
  DESCRIPTOR = _QUERY,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.Query)
  ))
_sym_db.RegisterMessage(Query)
_sym_db.RegisterMessage(Query.PassthroughDebugEntry)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), dict(

  ScoresEntry = _reflection.GeneratedProtocolMessageType('ScoresEntry', (_message.Message,), dict(
    DESCRIPTOR = _OBSERVATION_SCORESENTRY,
    __module__ = 'aqa_pb2'
    # @@protoc_insertion_point(class_scope:active_qa.Observation.ScoresEntry)
    ))
  ,
  DESCRIPTOR = _OBSERVATION,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.Observation)
  ))
_sym_db.RegisterMessage(Observation)
_sym_db.RegisterMessage(Observation.ScoresEntry)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  ObservationsEntry = _reflection.GeneratedProtocolMessageType('ObservationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_OBSERVATIONSENTRY,
    __module__ = 'aqa_pb2'
    # @@protoc_insertion_point(class_scope:active_qa.Response.ObservationsEntry)
    ))
  ,

  PassthroughDebugEntry = _reflection.GeneratedProtocolMessageType('PassthroughDebugEntry', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_PASSTHROUGHDEBUGENTRY,
    __module__ = 'aqa_pb2'
    # @@protoc_insertion_point(class_scope:active_qa.Response.PassthroughDebugEntry)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.ObservationsEntry)
_sym_db.RegisterMessage(Response.PassthroughDebugEntry)

EnvironmentRequest = _reflection.GeneratedProtocolMessageType('EnvironmentRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTREQUEST,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.EnvironmentRequest)
  ))
_sym_db.RegisterMessage(EnvironmentRequest)

EnvironmentResponse = _reflection.GeneratedProtocolMessageType('EnvironmentResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTRESPONSE,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.EnvironmentResponse)
  ))
_sym_db.RegisterMessage(EnvironmentResponse)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

QAInstance = _reflection.GeneratedProtocolMessageType('QAInstance', (_message.Message,), dict(
  DESCRIPTOR = _QAINSTANCE,
  __module__ = 'aqa_pb2'
  # @@protoc_insertion_point(class_scope:active_qa.QAInstance)
  ))
_sym_db.RegisterMessage(QAInstance)


_QUERY_PASSTHROUGHDEBUGENTRY._options = None
_OBSERVATION_SCORESENTRY._options = None
_RESPONSE_OBSERVATIONSENTRY._options = None
_RESPONSE_PASSTHROUGHDEBUGENTRY._options = None

_ENVIRONMENTSERVER = _descriptor.ServiceDescriptor(
  name='EnvironmentServer',
  full_name='active_qa.EnvironmentServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1530,
  serialized_end=1633,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetObservations',
    full_name='active_qa.EnvironmentServer.GetObservations',
    index=0,
    containing_service=None,
    input_type=_ENVIRONMENTREQUEST,
    output_type=_ENVIRONMENTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENVIRONMENTSERVER)

DESCRIPTOR.services_by_name['EnvironmentServer'] = _ENVIRONMENTSERVER

# @@protoc_insertion_point(module_scope)
