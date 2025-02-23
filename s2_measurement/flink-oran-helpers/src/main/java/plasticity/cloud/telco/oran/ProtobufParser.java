package plasticity.cloud.telco.oran;

import org.apache.flink.api.common.functions.RichMapFunction;
import org.o_ran_sc.ric.plt.a1med.msgs.MeasDataFile;

public class ProtobufParser extends RichMapFunction<String, MeasDataFile> {
    @Override
    public MeasDataFile map(String value) throws Exception {
        return MeasDataFile.parseFrom(value.getBytes());
    }
}
