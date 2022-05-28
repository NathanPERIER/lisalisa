package lat.elpainauchoco.lisalisa.userdata;

import lat.elpainauchoco.lisalisa.gamedata.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class WeaponAscensionLimit {

    private int level;     // 1-90
    private int ascension; // 0-6

    public WeaponAscensionLimit() { }

    public WeaponAscensionLimit(final GameDataService gdata) {
        int wl = gdata.getMaxWL();
        int ar = gdata.getMaxAR(wl);
        ascension = gdata.getMaxAscension(ar);
        level = gdata.getMaxLevel(ascension);
    }
}
