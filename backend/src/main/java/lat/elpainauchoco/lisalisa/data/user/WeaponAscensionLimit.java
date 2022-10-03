package lat.elpainauchoco.lisalisa.data.user;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class WeaponAscensionLimit extends AscensionLimits {

    public WeaponAscensionLimit() { }

    public WeaponAscensionLimit(final GameDataService gservice) {
        super(gservice);
    }
}
