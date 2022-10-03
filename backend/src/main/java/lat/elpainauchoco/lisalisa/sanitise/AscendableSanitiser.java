package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.user.Ascendable;
import lat.elpainauchoco.lisalisa.data.user.AscensionLimits;
import lat.elpainauchoco.lisalisa.data.user.UserConf;
import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;

public class AscendableSanitiser {

    protected final GameDataService gservice;
    protected final UserConf user;
    private final String asc_type;
    private final String asc_id;

    public AscendableSanitiser(final GameDataService gservice, final UserConf user, final String asc_type, final String asc_id) {
        this.gservice = gservice;
        this.asc_type = asc_type;
        this.asc_id   = asc_id;
        this.user     = user;
    }


    protected void sanitiseAscendable(final Ascendable ascendable) {
        sanitiseAscension(ascendable.getAscension(), user.getAdventureRank());
        sanitiseLevel(ascendable.getLevel(), ascendable.getAscension());
    }

    protected void sanitiseAscension(final int ascension, final int ar) {
        if(ascension < gservice.getMinAscension()) {
            throw new UserConfigException("Invalid ascension " + ascension
                    + " for " + asc_type + " " + asc_id
            );
        }
        if(ascension > gservice.getMaxAscension(ar)) {
            throw new UserConfigException("Invalid ascension " + ascension
                    + " at adventure rank " + ar
                    + " for " + asc_type + " " + asc_id
            );
        }
    }

    protected void sanitiseLevel(final int level, final int ascension) {
        if(level < gservice.getMinLevel(ascension) || level > gservice.getMaxLevel(ascension)) {
            throw new UserConfigException("Invalid weapon level " + level
                    + " at ascension " + ascension
                    + " for " + asc_type + " " + asc_id
            );
        }
    }


    protected void sanitiseLimits(final AscensionLimits limits) {
        if(limits == null) {
            return;
        }
        int ascension = limits.getAscension();
        if(ascension < gservice.getMinAscension() || ascension > gservice.getMaxAscension()) {
            throw new UserConfigException("Invalid ascension level " + ascension
                    + " in the limits of " + asc_type + " " + asc_id
            );
        }
        int level = limits.getLevel();
        if(level < gservice.getMinLevel(ascension) || level > gservice.getMaxLevel(ascension)) {
            throw new UserConfigException("Invalid character level " + level
                    + " with ascension " + ascension
                    + " in the limits of " + asc_type + " " + asc_id
            );
        }
    }

}
