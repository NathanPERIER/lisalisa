package lat.elpainauchoco.lisalisa.userdata;

import com.fasterxml.jackson.annotation.JsonProperty;
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

    public UserConf(String uid, String n, TravelerType tt) {
        id = uid;
        name = n;
        desc = "";
        profile = "traveler_" + tt.toString().toLowerCase() + "_anemo";
        namecard = "achievement_challenger";
        adventureRank = 1;
        worldLevel = 1;
        pity = new PityConf();
        limit = new UserDefaultLimits();
        characters = new HashMap<>();
        characters.put(profile, new CharacterConf(profile, this));
    }

    public enum TravelerType {
        BOY,
        GIRL
    }

}
