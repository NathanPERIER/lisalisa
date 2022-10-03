package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.game.WeaponData;
import lat.elpainauchoco.lisalisa.data.user.UserConf;
import lat.elpainauchoco.lisalisa.data.user.WeaponAscensionLimit;
import lat.elpainauchoco.lisalisa.data.user.WeaponConf;
import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;

public class WeaponConfSanitiser extends AscendableSanitiser {

    private final WeaponData data;
    private final WeaponConf weapon;
    private final String weaponType;

    public WeaponConfSanitiser(final GameDataService gservice, final WeaponConf weapon, final String uid, final UserConf user, final String weaponType) {
        super(gservice, user, "weapon", uid);
        this.weapon = weapon;
        final String weaponId = weapon.getId();
        if(!gservice.hasWeapon(weaponId)) {
            throw new UserConfigException("Weapon " + weaponId + " does not exist");
        }
        this.data = gservice.getWeapon(weaponId);
        this.weaponType = weaponType;
    }

    public void sanitise() {
        sanitiseType(data.getType());
        sanitiseAscendable(weapon);
        sanitiseWeaponRefinement(weapon.getRefinement());
        sanitiseWeaponLimits(weapon.getLimit());
    }

    protected void sanitiseType(String type) {
        if(weaponType != null && !weaponType.equals(type)) {
            throw new UserConfigException("Invalid weapon type " + type
                    + " for weapon " + ascUID
                    + "(expected " + weaponType + ")"
            );
        }
    }

    @Override
    protected void sanitiseAscension(int ascension, int ar) {
        super.sanitiseAscension(ascension, ar);
        if(ascension > data.getMaxAscension()) {
            throw new UserConfigException("Invalid weapon ascension " + ascension
                    + " for weapon " + ascUID
            );
        }
    }

    protected void sanitiseWeaponRefinement(final int refinement) {
        if(refinement < gservice.getMinRefinement() || refinement > data.getMaxRefinement()) {
            throw new UserConfigException("Invalid refinement value for weapon " + ascUID);
        }
    }

    protected void sanitiseWeaponLimits(final WeaponAscensionLimit limits) {
        sanitiseLimits(limits);
        if(limits.getAscension() > data.getMaxAscension()) {
            throw new UserConfigException("Invalid ascension level " + limits.getAscension()
                    + " in the limits of weapon " + ascUID
            );
        }
    }

}
