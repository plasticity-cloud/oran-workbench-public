# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: o-ran-sc-oam-meas-data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1co-ran-sc-oam-meas-data.proto\x12\x0cmeasurements\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"4\n\nFileSender\x12\x12\n\nsenderName\x18\x01 \x01(\t\x12\x12\n\nsenderType\x18\x02 \x01(\t\"C\n\x12\x46ileHeaderMeasData\x12-\n\tbeginTime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xaf\x01\n\nFileHeader\x12,\n\nfileSender\x18\x01 \x01(\x0b\x32\x18.measurements.FileSender\x12\x32\n\x08measData\x18\x02 \x01(\x0b\x32 .measurements.FileHeaderMeasData\x12\x19\n\x11\x66ileFormatVersion\x18\x03 \x01(\t\x12\x12\n\nvendorName\x18\x04 \x01(\t\x12\x10\n\x08\x64nPrefix\x18\x05 \x01(\t\"C\n\nMeasEntity\x12\x11\n\tuserLabel\x18\x01 \x01(\t\x12\x0f\n\x07localDn\x18\x02 \x01(\t\x12\x11\n\tswVersion\x18\x03 \x01(\t\"\x14\n\x03Job\x12\r\n\x05jobId\x18\x01 \x01(\t\"f\n\nGranPeriod\x12+\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x07\x65ndTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\tRepPeriod\x12+\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"#\n\x08MeasType\x12\t\n\x01p\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"W\n\nMeasResult\x12\x12\n\x08intValue\x18\x01 \x01(\x05H\x00\x12\x14\n\nfloatValue\x18\x02 \x01(\x02H\x00\x12\x15\n\x0bstringValue\x18\x03 \x01(\tH\x00\x42\x08\n\x06result\"7\n\x01R\x12\t\n\x01p\x18\x01 \x01(\r\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.measurements.MeasResult\"L\n\tMeasValue\x12\x12\n\nmeasObjLdn\x18\x01 \x01(\t\x12\x1a\n\x01r\x18\x02 \x03(\x0b\x32\x0f.measurements.R\x12\x0f\n\x07suspect\x18\x03 \x01(\x08\"\xee\x01\n\x08MeasInfo\x12\x12\n\nmeasInfoId\x18\x01 \x01(\t\x12\x1e\n\x03job\x18\x02 \x01(\x0b\x32\x11.measurements.Job\x12,\n\ngranPeriod\x18\x03 \x01(\x0b\x32\x18.measurements.GranPeriod\x12*\n\trepPeriod\x18\x04 \x01(\x0b\x32\x17.measurements.RepPeriod\x12(\n\x08measType\x18\x05 \x03(\x0b\x32\x16.measurements.MeasType\x12*\n\tmeasValue\x18\x06 \x03(\x0b\x32\x17.measurements.MeasValue\"n\n\x14MeasDataFileMeasData\x12,\n\nmeasEntity\x18\x01 \x01(\x0b\x32\x18.measurements.MeasEntity\x12(\n\x08measInfo\x18\x02 \x03(\x0b\x32\x16.measurements.MeasInfo\"A\n\x12\x46ileFooterMeasData\x12+\n\x07\x65ndTime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"@\n\nFileFooter\x12\x32\n\x08measData\x18\x01 \x01(\x0b\x32 .measurements.FileFooterMeasData\"\xa0\x01\n\x0cMeasDataFile\x12,\n\nfileHeader\x18\x01 \x01(\x0b\x32\x18.measurements.FileHeader\x12\x34\n\x08measData\x18\x02 \x03(\x0b\x32\".measurements.MeasDataFileMeasData\x12,\n\nfileFooter\x18\x03 \x01(\x0b\x32\x18.measurements.FileFooterb\x06proto3')



_FILESENDER = DESCRIPTOR.message_types_by_name['FileSender']
_FILEHEADERMEASDATA = DESCRIPTOR.message_types_by_name['FileHeaderMeasData']
_FILEHEADER = DESCRIPTOR.message_types_by_name['FileHeader']
_MEASENTITY = DESCRIPTOR.message_types_by_name['MeasEntity']
_JOB = DESCRIPTOR.message_types_by_name['Job']
_GRANPERIOD = DESCRIPTOR.message_types_by_name['GranPeriod']
_REPPERIOD = DESCRIPTOR.message_types_by_name['RepPeriod']
_MEASTYPE = DESCRIPTOR.message_types_by_name['MeasType']
_MEASRESULT = DESCRIPTOR.message_types_by_name['MeasResult']
_R = DESCRIPTOR.message_types_by_name['R']
_MEASVALUE = DESCRIPTOR.message_types_by_name['MeasValue']
_MEASINFO = DESCRIPTOR.message_types_by_name['MeasInfo']
_MEASDATAFILEMEASDATA = DESCRIPTOR.message_types_by_name['MeasDataFileMeasData']
_FILEFOOTERMEASDATA = DESCRIPTOR.message_types_by_name['FileFooterMeasData']
_FILEFOOTER = DESCRIPTOR.message_types_by_name['FileFooter']
_MEASDATAFILE = DESCRIPTOR.message_types_by_name['MeasDataFile']
FileSender = _reflection.GeneratedProtocolMessageType('FileSender', (_message.Message,), {
  'DESCRIPTOR' : _FILESENDER,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.FileSender)
  })
_sym_db.RegisterMessage(FileSender)

FileHeaderMeasData = _reflection.GeneratedProtocolMessageType('FileHeaderMeasData', (_message.Message,), {
  'DESCRIPTOR' : _FILEHEADERMEASDATA,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.FileHeaderMeasData)
  })
_sym_db.RegisterMessage(FileHeaderMeasData)

FileHeader = _reflection.GeneratedProtocolMessageType('FileHeader', (_message.Message,), {
  'DESCRIPTOR' : _FILEHEADER,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.FileHeader)
  })
_sym_db.RegisterMessage(FileHeader)

MeasEntity = _reflection.GeneratedProtocolMessageType('MeasEntity', (_message.Message,), {
  'DESCRIPTOR' : _MEASENTITY,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasEntity)
  })
_sym_db.RegisterMessage(MeasEntity)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.Job)
  })
_sym_db.RegisterMessage(Job)

GranPeriod = _reflection.GeneratedProtocolMessageType('GranPeriod', (_message.Message,), {
  'DESCRIPTOR' : _GRANPERIOD,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.GranPeriod)
  })
_sym_db.RegisterMessage(GranPeriod)

RepPeriod = _reflection.GeneratedProtocolMessageType('RepPeriod', (_message.Message,), {
  'DESCRIPTOR' : _REPPERIOD,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.RepPeriod)
  })
_sym_db.RegisterMessage(RepPeriod)

MeasType = _reflection.GeneratedProtocolMessageType('MeasType', (_message.Message,), {
  'DESCRIPTOR' : _MEASTYPE,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasType)
  })
_sym_db.RegisterMessage(MeasType)

MeasResult = _reflection.GeneratedProtocolMessageType('MeasResult', (_message.Message,), {
  'DESCRIPTOR' : _MEASRESULT,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasResult)
  })
_sym_db.RegisterMessage(MeasResult)

R = _reflection.GeneratedProtocolMessageType('R', (_message.Message,), {
  'DESCRIPTOR' : _R,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.R)
  })
_sym_db.RegisterMessage(R)

MeasValue = _reflection.GeneratedProtocolMessageType('MeasValue', (_message.Message,), {
  'DESCRIPTOR' : _MEASVALUE,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasValue)
  })
_sym_db.RegisterMessage(MeasValue)

MeasInfo = _reflection.GeneratedProtocolMessageType('MeasInfo', (_message.Message,), {
  'DESCRIPTOR' : _MEASINFO,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasInfo)
  })
_sym_db.RegisterMessage(MeasInfo)

MeasDataFileMeasData = _reflection.GeneratedProtocolMessageType('MeasDataFileMeasData', (_message.Message,), {
  'DESCRIPTOR' : _MEASDATAFILEMEASDATA,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasDataFileMeasData)
  })
_sym_db.RegisterMessage(MeasDataFileMeasData)

FileFooterMeasData = _reflection.GeneratedProtocolMessageType('FileFooterMeasData', (_message.Message,), {
  'DESCRIPTOR' : _FILEFOOTERMEASDATA,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.FileFooterMeasData)
  })
_sym_db.RegisterMessage(FileFooterMeasData)

FileFooter = _reflection.GeneratedProtocolMessageType('FileFooter', (_message.Message,), {
  'DESCRIPTOR' : _FILEFOOTER,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.FileFooter)
  })
_sym_db.RegisterMessage(FileFooter)

MeasDataFile = _reflection.GeneratedProtocolMessageType('MeasDataFile', (_message.Message,), {
  'DESCRIPTOR' : _MEASDATAFILE,
  '__module__' : 'o_ran_sc_oam_meas_data_pb2'
  # @@protoc_insertion_point(class_scope:measurements.MeasDataFile)
  })
_sym_db.RegisterMessage(MeasDataFile)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILESENDER._serialized_start=111
  _FILESENDER._serialized_end=163
  _FILEHEADERMEASDATA._serialized_start=165
  _FILEHEADERMEASDATA._serialized_end=232
  _FILEHEADER._serialized_start=235
  _FILEHEADER._serialized_end=410
  _MEASENTITY._serialized_start=412
  _MEASENTITY._serialized_end=479
  _JOB._serialized_start=481
  _JOB._serialized_end=501
  _GRANPERIOD._serialized_start=503
  _GRANPERIOD._serialized_end=605
  _REPPERIOD._serialized_start=607
  _REPPERIOD._serialized_end=663
  _MEASTYPE._serialized_start=665
  _MEASTYPE._serialized_end=700
  _MEASRESULT._serialized_start=702
  _MEASRESULT._serialized_end=789
  _R._serialized_start=791
  _R._serialized_end=846
  _MEASVALUE._serialized_start=848
  _MEASVALUE._serialized_end=924
  _MEASINFO._serialized_start=927
  _MEASINFO._serialized_end=1165
  _MEASDATAFILEMEASDATA._serialized_start=1167
  _MEASDATAFILEMEASDATA._serialized_end=1277
  _FILEFOOTERMEASDATA._serialized_start=1279
  _FILEFOOTERMEASDATA._serialized_end=1344
  _FILEFOOTER._serialized_start=1346
  _FILEFOOTER._serialized_end=1410
  _MEASDATAFILE._serialized_start=1413
  _MEASDATAFILE._serialized_end=1573
# @@protoc_insertion_point(module_scope)
