package lat.elpainauchoco.lisalisa.data.user;

import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class WeaponConf implements Ascendable {

    private String id;      // In the list of valid weapons
    private int level;      // 1-90 if rarity >= 3, else 1-70
    private int ascension;  // 0-6  if rarity >= 3, else 1-4
    private int refinement; // 1-5
    private WeaponAscensionLimit limit;

    public WeaponConf() { }

    public WeaponConf(String id, UserConf user, GameDataService gdata) {
        this.id = id;
        ascension = gdata.getMinAscension();
        level = gdata.getMinLevel(ascension);
        refinement = gdata.getMinRefinement();
        limit = user.getLimit().getWeapon();
    }

}
