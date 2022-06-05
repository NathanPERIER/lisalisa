package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lat.elpainauchoco.lisalisa.gamedata.GameDataService;
import lat.elpainauchoco.lisalisa.userdata.CharacterConf;
import lat.elpainauchoco.lisalisa.userdata.UserConf;

import java.util.Map;
import java.util.regex.Pattern;

public class UserConfSanitiser {

    private final Pattern USER_ID_REG = Pattern.compile("[1-9][0-9]{8}");
    private final Pattern USER_NAME_REG = Pattern.compile("[^\\n\\t\\r]+");

    private final GameDataService gservice;

    public UserConfSanitiser(final GameDataService gs) {
         gservice = gs;
    }

    public void sanitiseUser(final UserConf user) {
        sanitiseUserId(user.getId());
        sanitiseUserName(user.getName());
        // TODO description
        sanitiseWorldLevel(user.getWorldLevel());
        sanitiseAdventureRank(user.getAdventureRank(), user.getWorldLevel());
        sanitiseProfileCharacter(user.getProfile(), user.getCharacters());
        // TODO namecard
        // TODO pity
        // TODO limit
        sanitiseCharacters(user);
    }

    protected void sanitiseUserId(final String uid) {
        if(!USER_ID_REG.matcher(uid).matches()) {
            throw new UserConfigException("Bad user id format");
        }
    }

    protected void sanitiseUserName(final String username) {
        if(!USER_NAME_REG.matcher(username).matches()) {
            throw new UserConfigException("Bad username");
        }
    }

    protected void sanitiseWorldLevel(final int wl) {
        if(wl < gservice.getMinWL() || wl > gservice.getMaxWL()) {
            throw new UserConfigException("Bad world level " + wl);
        }
    }

    protected void sanitiseAdventureRank(final int ar, final int wl) {
        if(ar < gservice.getMinAR(wl) || ar > gservice.getMaxAR(wl)) {
            throw new UserConfigException("Bad adventure rank " + ar + " at world level " + wl);
        }
    }

    protected void sanitiseProfileCharacter(final String profile, final Map<String, CharacterConf> characters) {
        if(!characters.containsKey(profile)) {
            throw new UserConfigException("Profile character has to be owned by the user");
        }
    }

    protected void sanitiseCharacters(final UserConf user) {
        if(user.getCharacters() == null) {
            throw new UserConfigException("Character configuration cannot be null");
        }
        if(user.getCharacters().size() == 0) { // TODO at least one traveler, cannot mix boys and girls
            throw new UserConfigException("User has to have at least one character");
        }
        for(Map.Entry<String, CharacterConf> e : user.getCharacters().entrySet()) {
            sanitiseCharacter(e.getKey(), e.getValue(), user);
        }
    }

    protected void sanitiseCharacter(final String char_id, final CharacterConf character, final UserConf user) {
        // TODO check that character exists in the gservice
        if(character == null) {
            throw new UserConfigException("Configuration for character " + char_id + " cannot be null");
        }
        sanitiseCharacterAscension(char_id, character.getAscension(), user.getAdventureRank());
        sanitiseCharacterLevel(char_id, character.getLevel(), character.getAscension());
        sanitiseCharacterConstellations(char_id, character.getConstellations());
        sanitiseCharacterTalent(char_id, character.getNormalAttack(), "normal attack", character.getConstellations());
        sanitiseCharacterTalent(char_id, character.getElementalSkill(), "elemental skill", character.getConstellations());
        sanitiseCharacterTalent(char_id, character.getElementalBurst(), "elemental burst", character.getConstellations());
        // TODO weapon
        // TODO artifacts
        // TODO glider
        // TODO skin
        // TODO limit
    }

    public void sanitiseCharacterAscension(final String char_id, final int ascension, final int ar) {
        if(ascension < gservice.getMinAscension()) {
            throw new UserConfigException("Invalid character ascension " + ascension
                    + " for character " + char_id
            );
        }
        if(ascension > gservice.getMaxAscension(ar)) {
            throw new UserConfigException("Invalid character ascension " + ascension
                    + " at adventure rank " + ar
                    + " for character " + char_id
            );
        }
    }

    public void sanitiseCharacterLevel(final String char_id, final int level, final int ascension) {
        if(level < gservice.getMinLevel(ascension) || level > gservice.getMaxLevel(ascension)) {
            throw new UserConfigException("Invalid character level " + level
                    + " at ascension " + ascension
                    + " for character " + char_id
            );
        }
    }

    public void sanitiseCharacterConstellations(final String char_id, final int constellations) {
        if(constellations < gservice.getMaxConstellations() || constellations > gservice.getMaxConstellations()) {
            throw new UserConfigException("Invalid number of constellations for character " + char_id);
        }
    }

    public void sanitiseCharacterTalent(final String char_id, final int talentLevel, final String talentType,
                                        final int ascension) {
        if(talentLevel < gservice.getMinTalent()) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " for character " + char_id
            );
        }
        if(talentLevel > gservice.getMaxTalent(ascension)) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " at ascension " + ascension
                    + " for character " + char_id
            );
        }
    }


}
