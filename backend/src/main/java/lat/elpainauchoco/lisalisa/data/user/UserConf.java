package lat.elpainauchoco.lisalisa.data.user;

import com.fasterxml.jackson.annotation.JsonProperty;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;
import java.util.Map;

@Getter
@Setter
public class UserConf {

    private String id;
    private String name;
    private String desc;
    private String profile;
    private String namecard;
    @JsonProperty("adventure_rank")
    private int adventureRank;
    @JsonProperty("world_level")
    private int worldLevel;
    private PityConf pity;
    private UserDefaultLimits limit;
    private Map<String, CharacterConf> characters;

    public UserConf() { }

    public UserConf(final String uid, final String n, final TravelerType tt, final GameDataService gdata) {
        id = uid;
        name = n;
        desc = "";
        profile = "traveler_" + tt.toString().toLowerCase() + "_anemo";
        namecard = "achievement_challenger"; // TODO
        worldLevel = gdata.getMinWL();
        adventureRank = gdata.getMinAR(worldLevel);
        pity = new PityConf();
        limit = new UserDefaultLimits(gdata);
        characters = new HashMap<>();
        characters.put(profile, new CharacterConf(profile, this, gdata));
    }

    public enum TravelerType {
        BOY,
        GIRL
    }

}
