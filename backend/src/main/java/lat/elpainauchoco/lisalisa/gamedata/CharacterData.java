package lat.elpainauchoco.lisalisa.gamedata;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class CharacterData {

    private String weapon;
    private String defaultWeapon;
    private List<String> alternateSkins;
    private int increaseSkill;
    private int increaseBurst;

}
