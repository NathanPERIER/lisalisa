package lat.elpainauchoco.lisalisa.data.user;

import com.fasterxml.jackson.annotation.JsonProperty;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CharacterConf {

    private int level;          // 1-90
    private int ascension;      // 0-6
    @JsonProperty("normal_attack")
    private int normalAttack;   // 1-10
    @JsonProperty("elemental_skill")
    private int elementalSkill; // 1-10
    @JsonProperty("elemental_burst")
    private int elementalBurst; // 1-10
    private int constellations; // 0-6
    private String glider;      // In list of valid gliders
    private String skin;        // In list of valid alternate skins for the character, or "default"
    private CharacterAscensionLimit limit;
    private WeaponConf weapon;
    private ArtifactsConf artifacts;

    public CharacterConf() { }

    public CharacterConf(String id, UserConf user, GameDataService gdata) {
        ascension = gdata.getMinAscension();
        level = gdata.getMinLevel(ascension);
        normalAttack = gdata.getMinTalent();
        elementalSkill = normalAttack;
        elementalBurst = normalAttack;
        constellations = gdata.getMinConstellations();
        glider = "wings_of_first_flight"; // TODO first glider in the list
        skin = GameDataService.DEFAULT_CHARACTER_SKIN;
        limit = user.getLimit().getCharacter();
        final String defaultWeapon = gdata.getCharacter(id).getDefaultWeapon();
        weapon = new WeaponConf(defaultWeapon, user, gdata);
        artifacts = new ArtifactsConf();
    }

}
