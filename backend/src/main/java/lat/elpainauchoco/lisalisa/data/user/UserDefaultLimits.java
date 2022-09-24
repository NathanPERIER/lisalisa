package lat.elpainauchoco.lisalisa.data.user;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserDefaultLimits {

    private CharacterAscensionLimit character;
    private WeaponAscensionLimit weapon;

    public UserDefaultLimits() { }

    public UserDefaultLimits(final GameDataService gdata) {
        character = new CharacterAscensionLimit(gdata);
        weapon = new WeaponAscensionLimit(gdata);
    }

}
