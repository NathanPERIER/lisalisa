package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.game.WeaponData;
import lat.elpainauchoco.lisalisa.data.user.UserConf;
import lat.elpainauchoco.lisalisa.data.user.WeaponAscensionLimit;
import lat.elpainauchoco.lisalisa.data.user.WeaponConf;
import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lombok.Getter;

public class WeaponConfSanitiser extends AscendableSanitiser {

    private final String weapon_id;
    private final WeaponConf weapon;
    @Getter
    private final WeaponData data;

    public WeaponConfSanitiser(final GameDataService gservice, final WeaponConf weapon, final UserConf user) {
        super(gservice, user, "weapon", weapon.getId());
        this.weapon = weapon;
        this.weapon_id = weapon.getId();
        if(!gservice.hasWeapon(weapon_id)) {
            throw new UserConfigException("Weapon " + weapon_id + " does not exist");
        }
        this.data = gservice.getWeapon(weapon_id);
    }

    public void sanitise() {
        sanitiseAscendable(weapon);
        sanitiseWeaponRefinement(weapon.getRefinement());
        sanitiseWeaponLimits(weapon.getLimit());
    }

    @Override
    protected void sanitiseAscension(int ascension, int ar) {
        super.sanitiseAscension(ascension, ar);
        if(ascension > data.getMaxAscension()) {
            throw new UserConfigException("Invalid weapon ascension " + ascension
                    + " for weapon " + weapon_id
            );
        }
    }

    public void sanitiseWeaponRefinement(final int refinement) {
        if(refinement < gservice.getMinRefinement() || refinement > data.getMaxRefinement()) {
            throw new UserConfigException("Invalid refinement value for weapon " + weapon_id);
        }
    }

    public void sanitiseWeaponLimits(final WeaponAscensionLimit limits) {
        sanitiseLimits(limits);
        if(limits.getAscension() > data.getMaxAscension()) {
            throw new UserConfigException("Invalid ascension level " + limits.getAscension()
                    + " in the limits of weapon " + weapon_id
            );
        }
    }

}
