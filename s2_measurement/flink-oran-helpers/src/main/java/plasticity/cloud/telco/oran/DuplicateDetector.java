package plasticity.cloud.telco.oran;

import org.apache.flink.api.common.functions.RichMapFunction;
import org.apache.flink.api.common.state.ValueState;
import org.apache.flink.api.common.state.ValueStateDescriptor;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.configuration.Configuration;
import org.o_ran_sc.ric.plt.a1med.msgs.MeasDataFile;

public class DuplicateDetector extends RichMapFunction<MeasDataFile, Tuple2<String, Integer>> {
    private ValueState<Boolean> seen;

    @Override
    public void open(Configuration parameters) {
        ValueStateDescriptor<Boolean> descriptor = 
            new ValueStateDescriptor<>("seen", Boolean.class);
        seen = getRuntimeContext().getState(descriptor);
    }

    @Override
    public Tuple2<String, Integer> map(MeasDataFile event) throws Exception {
        String userLabel = event.getMeasData(0).getMeasEntity().getUserLabel();
        
        if (seen.value() == null) {
            seen.update(true);
            return new Tuple2<>(userLabel, 0);
        }
        return new Tuple2<>(userLabel, 1);
    }
}
