package lat.elpainauchoco.lisalisa.userdata;

/*
"artifacts": {
    "circlet": {
        "rarity": 5,
        "set": "viridescent_venerer"
    },
    "flower": {
        "rarity": 5,
        "set": "viridescent_venerer"
    },
    "goblet": {
        "rarity": 5,
        "set": "viridescent_venerer"
    },
    "plume": {
        "rarity":5,
        "set": "viridescent_venerer"
    },
    "timepiece": {
        "rarity":5,
        "set": "viridescent_venerer"
    }
}
*/

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ArtifactsConf {

    private ArtifactConf circlet;
    private ArtifactConf flower;
    private ArtifactConf goblet;
    private ArtifactConf plume;
    private ArtifactConf timepiece;

    public ArtifactsConf() {
        circlet = null;
        flower = null;
        goblet = null;
        plume = null;
        timepiece = null;
    }

    @Getter
    @Setter
    public static class ArtifactConf {

        private int rarity;   // 1-5 (depends on the set)
        private String set;   // In the list of valid sets, also depends on the type of piece
        // TODO stats and substats
        @JsonProperty("is_good")
        private boolean good;

    }

}
