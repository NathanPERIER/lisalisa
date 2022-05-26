package lat.elpainauchoco.lisalisa.userdata;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class WeaponConf {

    private String id;      // In the list of valid weapons
    private int level;      // 1-90 if rarity >= 3, else 1-70
    private int ascension;  // 0-6  if rarity >= 3, else 1-4
    private int refinement; // 1-5
    private WeaponAscensionLimit limit;

    public WeaponConf() { }

    public WeaponConf(String id, UserConf user) {
        this.id = id;
        // Temporary, a generic system would be better
        level = 1;
        ascension = 0;
        refinement = 1;
        limit = user.getLimit().getWeapon();
    }

}
