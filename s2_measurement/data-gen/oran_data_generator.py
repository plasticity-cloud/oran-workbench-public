import random
from datetime import datetime, timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.duration_pb2 import Duration
import avro.schema
from avro.io import DatumWriter, BinaryEncoder
import io
import os
import uuid

# First, we need to generate the protobuf classes using the schema
# Assuming the protobuf classes are generated and imported as:
from measurement_pb2 import MeasDataFile, FileSender, FileHeader, FileHeaderMeasData, \
    MeasEntity, MeasInfo, MeasType, MeasValue, R, MeasResult, Job, GranPeriod, RepPeriod, \
    FileFooter, FileFooterMeasData, MeasDataFileMeasData

class OranDataGenerator:
    def __init__(self):
        self.measurement_types = [
            ("RRU.PowerConsumption", "float"),
            ("RRU.Temperature", "float"),
            ("RRU.CPUUsage", "float"),
            ("RRU.ThroughputDL", "int"),
            ("RRU.ThroughputUL", "int"),
            ("RRU.ActiveUsers", "int"),
            ("RRU.ErrorCount", "int"),
            ("RRU.Status", "string")
        ]
        
    def _create_timestamp(self, dt):
        ts = Timestamp()
        ts.FromDatetime(dt)
        return ts
    
    def _create_duration(self, seconds):
        duration = Duration()
        duration.seconds = seconds
        return duration
    
    def _generate_measure_result(self, mtype):
        result = MeasResult()
        if mtype[1] == "float":
            result.floatValue = random.uniform(0, 100)
        elif mtype[1] == "int":
            result.intValue = random.randint(0, 1000)
        else:
            statuses = ["OK", "WARNING", "ERROR", "MAINTENANCE"]
            result.stringValue = random.choice(statuses)
        return result
    
    def generate_measurement_data(self, num_entities=2, measurements_per_entity=100):
        now = datetime.now()
        
        # Create file header
        file_header = FileHeader(
            fileSender=FileSender(
                senderName="O-RAN-Generator",
                senderType="RRU"
            ),
            measData=FileHeaderMeasData(
                beginTime=self._create_timestamp(now)
            ),
            fileFormatVersion="1.0",
            vendorName="OpenRAN-Vendor",
            dnPrefix="RRU-Site-1"
        )
        
        # Create measurement data
        meas_data_list = []
        for entity_idx in range(num_entities):
            meas_entity = MeasEntity(
                userLabel=f"RRU-{entity_idx+1}",
                localDn=f"RRU-Site-1/RRU-{entity_idx+1}",
                swVersion="v2.1.0"
            )
            
            # Create measurement info
            meas_info = MeasInfo(
                measInfoId=str(uuid.uuid4()),
                job=Job(jobId=f"job-{entity_idx+1}"),
                granPeriod=GranPeriod(
                    duration=self._create_duration(300),  # 5 minutes
                    endTime=self._create_timestamp(now + timedelta(minutes=5))
                ),
                repPeriod=RepPeriod(
                    duration=self._create_duration(3600)  # 1 hour
                )
            )
            
            # Add measurement types
            meas_info.measType.extend([
                MeasType(p=i+1, name=mtype[0])
                for i, mtype in enumerate(self.measurement_types)
            ])
            
            # Generate measurement values
            for _ in range(measurements_per_entity):
                meas_value = MeasValue(
                    measObjLdn=f"RRU-Site-1/RRU-{entity_idx+1}/CELL-{random.randint(1,3)}",
                    suspect=random.random() < 0.1  # 10% chance of suspect data
                )
                
                # Generate results for each measurement type
                for i, mtype in enumerate(self.measurement_types):
                    r = R(
                        p=i+1,
                        value=self._generate_measure_result(mtype)
                    )
                    meas_value.r.append(r)
                
                meas_info.measValue.append(meas_value)
            
            meas_data = MeasDataFileMeasData(
                measEntity=meas_entity
            )
            meas_data.measInfo.append(meas_info)
            meas_data_list.append(meas_data)
        
        # Create file footer
        file_footer = FileFooter(
            measData=FileFooterMeasData(
                endTime=self._create_timestamp(now + timedelta(hours=1))
            )
        )
        
        # Create final message
        return MeasDataFile(
            fileHeader=file_header,
            measData=meas_data_list,
            fileFooter=file_footer
        )

    def save_to_protobuf(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(data.SerializeToString())

    def read_from_protobuf(self, filename):
        with open(filename, 'rb') as f:
            data = MeasDataFile()
            data.ParseFromString(f.read())
            return data
