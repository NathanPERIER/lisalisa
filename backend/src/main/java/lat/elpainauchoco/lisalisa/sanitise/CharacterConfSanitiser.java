package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lat.elpainauchoco.lisalisa.gamedata.GameDataService;
import lat.elpainauchoco.lisalisa.userdata.CharacterConf;
import lat.elpainauchoco.lisalisa.userdata.UserConf;

public class CharacterConfSanitiser {

    private final GameDataService gservice;

    public CharacterConfSanitiser(final GameDataService gs) {
        gservice = gs;
    }

    public void sanitiseCharacter(final String char_id, final CharacterConf character, final UserConf user) {
        // TODO check that character exists in the gservice
        if(character == null) {
            throw new UserConfigException("Configuration for character " + char_id + " cannot be null");
        }
        sanitiseCharacterAscension(char_id, character.getAscension(), user.getAdventureRank());
        sanitiseCharacterLevel(char_id, character.getLevel(), character.getAscension());
        sanitiseCharacterConstellations(char_id, character.getConstellations());
        sanitiseCharacterTalent(char_id, character.getNormalAttack(), "normal attack", character.getAscension());
        sanitiseCharacterTalent(char_id, character.getElementalSkill(), "elemental skill", character.getAscension());
        sanitiseCharacterTalent(char_id, character.getElementalBurst(), "elemental burst", character.getAscension());
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
