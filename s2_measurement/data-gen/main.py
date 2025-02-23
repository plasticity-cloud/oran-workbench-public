from oran_data_generator import OranDataGenerator

def main():
    # Create data generator
    generator = OranDataGenerator()
    
    num_entities_rru=12000
    measurements_per_rru=1000
    
    # Generate sample data
    data = generator.generate_measurement_data(
        num_entities=num_entities_rru,          # Number of RRU entities
        measurements_per_entity=measurements_per_rru  # Number of measurements per entity
    )
    
    # Save to protobuf file
    protobuf_filename = "measurement_data" + (str) num_entities_rru + _ + (str) measurements_per_rru + ".pb"
    generator.save_to_protobuf(data, protobuf_filename)
    
    print(f"Generated protobuf file: {protobuf_filename}")

if __name__ == "__main__":
    main()
