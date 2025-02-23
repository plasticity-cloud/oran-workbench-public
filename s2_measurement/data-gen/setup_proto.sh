pip install protobuf avro-python3


sudo dnf install protobuf-devel

mkdir -p google/protobuf
curl -o google/protobuf/duration.proto https://raw.githubusercontent.com/protocolbuffers/protobuf/main/src/google/protobuf/duration.proto
curl -o google/protobuf/timestamp.proto https://raw.githubusercontent.com/protocolbuffers/protobuf/main/src/google/protobuf/timestamp.proto

protoc --python_out=. o-ran-sc-oam-meas-data.proto
