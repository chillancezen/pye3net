# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ether_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ether_service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x65ther_service.proto\x1a\x0c\x63ommon.proto\"F\n\x15req_ether_service_key\x12\x12\n\nper_tenant\x18\x01 \x01(\x08\x12\x19\n\x11tenant_id_or_uuid\x18\x02 \x01(\t\"}\n\x11res_ether_service\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cservice_type\x18\x03 \x01(\t\x12\x11\n\ttenant_id\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\x12\x11\n\tlink_type\x18\x06 \x01(\t2\xb0\x03\n\rether_service\x12\x45\n\x15rpc_get_ether_service\x12\x16.req_ether_service_key\x1a\x12.res_ether_service\"\x00\x12K\n\x17rpc_list_ether_services\x12\x16.req_ether_service_key\x1a\x12.res_ether_service\"\x00(\x01\x30\x01\x12\x46\n\x1arpc_register_ether_service\x12\x12.res_ether_service\x1a\x12.res_ether_service\"\x00\x12?\n\x1crpc_unregister_ether_service\x12\x16.req_ether_service_key\x1a\x05.null\"\x00\x12\x37\n\x16rpc_push_ether_service\x12\x12.res_ether_service\x1a\x05.null\"\x00(\x01\x12I\n\x17rpc_pull_ether_services\x12\x16.req_ether_service_key\x1a\x12.res_ether_service\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_REQ_ETHER_SERVICE_KEY = _descriptor.Descriptor(
  name='req_ether_service_key',
  full_name='req_ether_service_key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='per_tenant', full_name='req_ether_service_key.per_tenant', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenant_id_or_uuid', full_name='req_ether_service_key.tenant_id_or_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=107,
)


_RES_ETHER_SERVICE = _descriptor.Descriptor(
  name='res_ether_service',
  full_name='res_ether_service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='res_ether_service.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='res_ether_service.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_type', full_name='res_ether_service.service_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenant_id', full_name='res_ether_service.tenant_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='res_ether_service.created_at', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_type', full_name='res_ether_service.link_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=234,
)

DESCRIPTOR.message_types_by_name['req_ether_service_key'] = _REQ_ETHER_SERVICE_KEY
DESCRIPTOR.message_types_by_name['res_ether_service'] = _RES_ETHER_SERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

req_ether_service_key = _reflection.GeneratedProtocolMessageType('req_ether_service_key', (_message.Message,), dict(
  DESCRIPTOR = _REQ_ETHER_SERVICE_KEY,
  __module__ = 'ether_service_pb2'
  # @@protoc_insertion_point(class_scope:req_ether_service_key)
  ))
_sym_db.RegisterMessage(req_ether_service_key)

res_ether_service = _reflection.GeneratedProtocolMessageType('res_ether_service', (_message.Message,), dict(
  DESCRIPTOR = _RES_ETHER_SERVICE,
  __module__ = 'ether_service_pb2'
  # @@protoc_insertion_point(class_scope:res_ether_service)
  ))
_sym_db.RegisterMessage(res_ether_service)



_ETHER_SERVICE = _descriptor.ServiceDescriptor(
  name='ether_service',
  full_name='ether_service',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=237,
  serialized_end=669,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpc_get_ether_service',
    full_name='ether_service.rpc_get_ether_service',
    index=0,
    containing_service=None,
    input_type=_REQ_ETHER_SERVICE_KEY,
    output_type=_RES_ETHER_SERVICE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_list_ether_services',
    full_name='ether_service.rpc_list_ether_services',
    index=1,
    containing_service=None,
    input_type=_REQ_ETHER_SERVICE_KEY,
    output_type=_RES_ETHER_SERVICE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_register_ether_service',
    full_name='ether_service.rpc_register_ether_service',
    index=2,
    containing_service=None,
    input_type=_RES_ETHER_SERVICE,
    output_type=_RES_ETHER_SERVICE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_unregister_ether_service',
    full_name='ether_service.rpc_unregister_ether_service',
    index=3,
    containing_service=None,
    input_type=_REQ_ETHER_SERVICE_KEY,
    output_type=common__pb2._NULL,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_push_ether_service',
    full_name='ether_service.rpc_push_ether_service',
    index=4,
    containing_service=None,
    input_type=_RES_ETHER_SERVICE,
    output_type=common__pb2._NULL,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_pull_ether_services',
    full_name='ether_service.rpc_pull_ether_services',
    index=5,
    containing_service=None,
    input_type=_REQ_ETHER_SERVICE_KEY,
    output_type=_RES_ETHER_SERVICE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ETHER_SERVICE)

DESCRIPTOR.services_by_name['ether_service'] = _ETHER_SERVICE

# @@protoc_insertion_point(module_scope)
