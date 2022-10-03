package lat.elpainauchoco.lisalisa.data.user;

import com.fasterxml.jackson.annotation.JsonProperty;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CharacterAscensionLimit extends AscensionLimits {

    @JsonProperty("normal_attack")
    private int normalAttack;   // 1-10
    @JsonProperty("elemental_skill")
    private int elementalSkill; // 1-10
    @JsonProperty("elemental_burst")
    private int elementalBurst; // 1-10

    public CharacterAscensionLimit() { }

    public CharacterAscensionLimit(final GameDataService gservice) {
        super(gservice);
        normalAttack = gservice.getMaxTalent(ascension);
        elementalSkill = normalAttack;
        elementalBurst = normalAttack;
    }

}
