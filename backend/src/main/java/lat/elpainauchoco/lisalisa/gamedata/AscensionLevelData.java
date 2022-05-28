package lat.elpainauchoco.lisalisa.gamedata;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

public class AscensionLevelData {

    @Getter
    @Setter
    private int maxTalent;
    @Getter
    @JsonIgnore
    private int minLevel;
    @Getter
    @JsonIgnore
    private int maxLevel;

    @JsonProperty
    public void setLevel(final int[] level) {
        minLevel = level[0];
        maxLevel = level[1];
    }

}
