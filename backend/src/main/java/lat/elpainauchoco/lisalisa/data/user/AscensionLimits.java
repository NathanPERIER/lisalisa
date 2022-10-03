package lat.elpainauchoco.lisalisa.data.user;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
abstract class AscensionLimits {

    protected int level;     // 1-90
    protected int ascension; // 0-6

    public AscensionLimits() { }

    public AscensionLimits(final GameDataService gservice) {
        int wl = gservice.getMaxWL();
        int ar = gservice.getMaxAR(wl);
        ascension = gservice.getMaxAscension(ar);
        level = gservice.getMaxLevel(ascension);
    }

}
