package lat.elpainauchoco.lisalisa.data.user;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

import java.util.Map;

@Getter
@Setter
public class ArtifactsConf {

    private ArtifactConf circlet;
    private ArtifactConf flower;
    private ArtifactConf goblet;
    private ArtifactConf plume;
    private ArtifactConf sands;

    public ArtifactsConf() {
        circlet = null;
        flower = null;
        goblet = null;
        plume = null;
        sands = null;
    }

    @Getter
    @Setter
    public static class ArtifactConf {

        private String set;   // In the list of valid sets, also depends on the type of piece
        private String type;  // circlet, flower, goblet, plume or sands
        private int rarity;   // 1-5  (depends on the set)
        private int level;    // 0-20 (depends on the rarity)
        @JsonProperty("is_good")
        private boolean good;
        @JsonProperty("main_stat")
        private String mainStat;
        private Map<String,Double> substats;

    }

}
