package lat.elpainauchoco.lisalisa.data.game;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

public class AdventureRankData {

    @JsonIgnore
    private int beginRange;
    @JsonIgnore
    private int endRange;
    @Getter
    @Setter
    @JsonProperty("ascension")
    private int maxAscension;

    @JsonProperty
    public void setRange(int[] range) {
        beginRange = range[0];
        endRange = range[1];
    }

    public boolean inRange(int advRank) {
        return advRank >= beginRange && advRank <= endRange;
    }

}
