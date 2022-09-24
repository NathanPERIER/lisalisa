package lat.elpainauchoco.lisalisa.data.game;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
public class CharacterData {

    private String weapon;
    private String defaultWeapon;
    private List<String> alternateSkins;
    private int increaseSkill; // TODO remove (actually useless)
    private int increaseBurst; // TODO remove (actually useless)

}
