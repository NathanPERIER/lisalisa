package lat.elpainauchoco.lisalisa.userdata;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CharacterAscensionLimit {

    private int level;          // 1-90
    private int ascension;      // 0-6
    @JsonProperty("normal_attack")
    private int normalAttack;   // 1-10
    @JsonProperty("elemental_skill")
    private int elementalSkill; // 1-10
    @JsonProperty("elemental_burst")
    private int elementalBurst; // 1-10

}
