package lat.elpainauchoco.lisalisa.userdata;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CharacterAscensionLimit {

    private int normalAttack;   // 1-10
    private int elementalSkill; // 1-10
    private int elementalBurst; // 1-10
    private int ascension;      // 1-6
    private int level;          // 1-90

}
