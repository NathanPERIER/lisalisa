package lat.elpainauchoco.lisalisa.data.game;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

import java.util.Map;
import java.util.Set;

public class ArtifactRarityData {

    @Getter
    @Setter
    @JsonProperty("ascension")
    private int maxLevel;
    @Getter
    @Setter
    @JsonProperty("ascension")
    private int maxSubstats;
    private Map<String, Float[]> props;

    public Set<String> getSubstats() {
        return props.keySet();
    }

    public Float[] getProps(String substat) {
        return props.get(substat);
    }

}
