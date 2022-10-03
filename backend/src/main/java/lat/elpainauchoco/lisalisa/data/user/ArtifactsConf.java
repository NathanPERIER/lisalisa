package lat.elpainauchoco.lisalisa.data.user;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.Map;

@Getter
@Setter
public class ArtifactsConf {

    private ArtifactPieceConf circlet;
    private ArtifactPieceConf flower;
    private ArtifactPieceConf goblet;
    private ArtifactPieceConf plume;
    private ArtifactPieceConf sands;

    public ArtifactsConf() {
        circlet = null;
        flower = null;
        goblet = null;
        plume = null;
        sands = null;
    }

    public Map<String, ArtifactPieceConf> toMapping() {
        Map<String, ArtifactPieceConf> res = new HashMap<>();
        res.put("circlet", circlet);
        res.put("flower", flower);
        res.put("goblet", goblet);
        res.put("plume", plume);
        res.put("sands", sands);
        return res;
    }

    @Getter
    @Setter
    public static class ArtifactPieceConf {

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
