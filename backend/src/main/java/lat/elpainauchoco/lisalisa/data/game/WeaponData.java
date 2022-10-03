package lat.elpainauchoco.lisalisa.data.game;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class WeaponData {

    private String type;
    private int rarity;
    @JsonProperty("ascension")
    private int maxAscension;
    @JsonProperty("refinement")
    private int maxRefinement;

}
