package lat.elpainauchoco.lisalisa.userdata;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.HashMap;
import java.util.Map;

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
        characters = new HashMap<>();
    }

    public String getName() {
        return name;
    }

    public void setName(final String n) {
        name = n;
    }

    public String getId() {
        return id;
    }

    public void setId(final String uid) {
        id = uid;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(final String d) {
        desc = d;
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(final String p) {
        profile = p;
    }

    public String getNamecard() {
        return namecard;
    }

    public void setNamecard(final String nc) {
        namecard = nc;
    }

    public int getAdventureRank() {
        return adventureRank;
    }

    public void setNamecard(final int ar) {
        adventureRank = ar;
    }

    public int getWorldLevel() {
        return worldLevel;
    }

    public void setWorldLevel(final int wl) {
        worldLevel = wl;
    }

    public PityConf getPity() {
        return pity;
    }

    public void setPity(final PityConf pc) {
        pity = pc;
    }

    public Map<String, CharacterConf> getCharacters() {
        return characters;
    }

    public void setCharacters(final Map<String, CharacterConf> chars) {
        characters = chars;
    }


    public enum TravelerType {
        BOY,
        GIRL
    }

}
