package plasticity.cloud.telco.oran;

import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.functions.RichMapFunction;
import org.apache.flink.api.common.state.ValueState;
import org.apache.flink.api.common.state.ValueStateDescriptor;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.configuration.Configuration;
import org.apache.flink.connector.file.src.FileSource;
import org.apache.flink.connector.file.src.reader.TextLineInputFormat;
import org.apache.flink.core.fs.Path;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.TumblingProcessingTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.o_ran_sc.ric.plt.a1med.msgs.MeasDataFile;

// Rest of the code remains the same...


public class DuplicateEventCounter {

    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: DuplicateEventCounter <input-path>");
            System.exit(1);
        }

        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // Create file source
        FileSource<String> source = FileSource.forRecordStreamFormat(
            new TextLineInputFormat(),
            new Path(args[0]))
            .build();

        // Create the data stream from file source
        DataStream<String> inputStream = env.fromSource(
            source,
            WatermarkStrategy.noWatermarks(),
            "File Source"
        );

        // Process the stream
        DataStream<Tuple2<String, Integer>> duplicateCounts = inputStream
            .map(new ProtobufParser())
            .keyBy(event ->  event.getMeasData(0).getMeasEntity().getUserLabel())
            .map(new DuplicateDetector())
            .keyBy(tuple -> tuple.f0)
            .window(TumblingProcessingTimeWindows.of(Time.minutes(1)))
            .sum(1);

        // Print results
        duplicateCounts.print();

        env.execute("O-RAN Event Duplicate Counter");
    }
}
